# Código original obtido pelo site do serpro https://www.serpro.gov.br/menu/noticias/noticias-2024/cnpj-alfanumerico

* Este código foi atualizado com ajuda do ChatGPT para ser usado em um único arquivo, para verificar os CNPJ Normais e Alfanumericos com ou sem mascara.
    Vc é mais folgado do que eu rsrsrs

# Criar uma instância do CNPJ

* CNPJ completo com ou sem máscara
cnpj = CNPJ("12.ABC.345/01DE-35") /n
cnpj = CNPJ("12ABC34501DE35") /n
cnpj = CNPJ("00.000.000/0001-91")
cnpj = CNPJ("000000000001")

* CNPJ sem Dígito Verificador
cnpj_sem_dv = CNPJ("12.ABC.345/01DE")
cnpj_sem_dv = CNPJ("12ABC34501DE")
cnpj_sem_dv = CNPJ("00.000.000/0001")
cnpj_sem_dv = CNPJ("000000000001")

# Validar o CNPJ
* print("Validação:", cnpj.valida())  # Retorna True ou False

# Gerar DV para um CNPJ sem dígitos verificadores
* print("Gerar DV:", cnpj_sem_dv.gera_dv())

## ou pode utilizar o terminal

### Exemplo de execução do gerador de dígito verificador
python.exe cnpjauth.py -dv 12ABC34501DE35 # Teremos como resposta o dígito verificador: 35

### Exemplo com CNPJ válido ou não
python.exe cnpjauth.py -v 12ABC34501DE35 # Teremos como resposta: True
