import re
from math import ceil
import sys

"""
Código original obtido pelo site do serpro https://www.serpro.gov.br/menu/noticias/noticias-2024/cnpj-alfanumerico

Este código foi atualizado com ajuda do ChatGPT para ser usado em um único arquivo, para verificar os CNPJ Normais e Alfanumericos com ou sem mascara.
    Vc é mais folgado do que eu rsrsrs

# Criar uma instância do CNPJ

cnpj = CNPJ("12.ABC.345/01DE-35")
# cnpj = CNPJ("12ABC34501DE35")
# cnpj = CNPJ("00.000.000/0001-91")
# cnpj = CNPJ("000000000001")
# cnpj_sem_dv = CNPJ("12.ABC.345/01DE")

cnpj_sem_dv = CNPJ("12ABC34501DE")
# cnpj_sem_dv = CNPJ("00.000.000/0001")
# cnpj_sem_dv = CNPJ("000000000001")

# Validar o CNPJ
print("Validação:", cnpj.valida())  # Retorna True ou False

# Gerar DV para um CNPJ sem dígitos verificadores
print("Gerar DV:", cnpj_sem_dv.gera_dv())

ou pode utilizar o terminal

### Exemplo de execução do gerador de dígito verificador
python.exe cnpjauth.py -dv 12ABC34501DE35 # Teremos como resposta o dígito verificador: 35

### Exemplo com CNPJ válido ou não
python.exe cnpjauth.py -v 12ABC34501DE35 # Teremos como resposta: True

"""

class DigitoVerificador:
    def __init__(self, _input):
        self._cnpj = _input.upper()
        self._pesos = list()
        self.digito = 0

    def calculaAscii(self, _caracter):
        return ord(_caracter) - 48

    def calcula_soma(self):
        _tamanho_range = len(self._cnpj)
        _num_range = ceil(_tamanho_range / 8)
        for i in range(_num_range):
            self._pesos.extend(range(2, 10))
        self._pesos = self._pesos[0:_tamanho_range]
        self._pesos.reverse()
        sum_of_products = sum(
            a * b for a, b in zip(map(self.calculaAscii, self._cnpj), self._pesos)
        )
        return sum_of_products

    def calcula(self):
        mod_sum = self.calcula_soma() % 11
        if mod_sum < 2:
            return 0
        else:
            return 11 - mod_sum


class CNPJ:
    def __init__(self, _input_cnpj):
        try:
            _cnpj_valido = self.__valida_formato(_input_cnpj)
            if _cnpj_valido:
                self.cnpj = self.__remove_pontuacao(_input_cnpj)
            else:
                raise ValueError(
                    "CNPJ não está no padrão 12BC345001DE35 ou 12.BC3.450/01DE-35 (Para validação), "
                    "ou 12BC345001DE ou 12.BC3.450/01DE (Para geração do DV)."
                )
        except ValueError as e:
            raise ValueError(e)

    def __remove_digitos_cnpj(self):
        if len(self.cnpj) == 14:
            self.cnpj_sem_dv = self.cnpj[0:-2]
        elif len(self.cnpj) == 12:
            self.cnpj_sem_dv = self.cnpj
        else:
            raise ValueError("CNPJ com tamanho inválido!")

    def __remove_pontuacao(self, _input):
        # Remove caracteres não alfanuméricos
        return ''.join(x for x in _input if x.isalnum())

    def valida(self):
        self.__remove_digitos_cnpj()
        _dv = self.gera_dv()
        return f"{self.cnpj_sem_dv}{_dv}" == self.cnpj

    def gera_dv(self):
        self.__remove_digitos_cnpj()
        dv1 = DigitoVerificador(self.cnpj_sem_dv)
        dv1char = str(dv1.calcula())
        dv2 = DigitoVerificador(self.cnpj_sem_dv + dv1char)
        dv2char = str(dv2.calcula())
        return f"{dv1char}{dv2char}"

    def __valida_formato(self, _cnpj):
        # Remove pontuação para validar o formato
        _cnpj = self.__remove_pontuacao(_cnpj)
        # Aceita formatos:
        # - Numérico puro (12 ou 14 caracteres)
        # - Alfanumérico puro (12 ou 14 caracteres)
        # - Formato pontuado com ou sem DV
        return re.match(
            r'^\d{12}$|^\d{14}$|^[A-Z\d]{12}$|^[A-Z\d]{14}$|^[A-Z\d]{2}\.[A-Z\d]{3}\.[A-Z\d]{3}/[A-Z\d]{4}(-[A-Z\d]{2})?$',
            _cnpj
        )


if __name__ == "__main__":
    try:
        if len(sys.argv) < 3:
            raise ValueError("Formato inválido do CNPJ.")
        _exec = sys.argv[1].upper()
        _input = sys.argv[2]

        cnpj = CNPJ(_input)
        if _exec == '-V':
            print(cnpj.valida())
        elif _exec == '-DV':
            print(cnpj.gera_dv())
        else:
            raise ValueError(
                "Opção inválida passada, as válidas são: -v para validar, -dv para gerar dígito validador."
            )
    except Exception as e:
        print(e)
