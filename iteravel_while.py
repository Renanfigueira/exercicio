frase = 'eu amo batata frita com ketchup'
i = 0
qtd_letra = 0
letra_ma = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_letra_ma = frase.count(letra_atual)

    if qtd_letra < qtd_letra_ma:
        qtd_letra = qtd_letra_ma
        letra_ma = letra_atual

    i += 1

print(f'A letra que mais apareceu foi: {letra_ma}, e a quantidade é {qtd_letra}')