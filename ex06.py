preco = float(input("qual e o preço: "))#atribui nome e valor a sua variaveis
quantidade = int(input("qual a quantidade de itens pego: "))
valor_pago = float(input("qual foi o valor pago: "))

total = preco * quantidade#faz um calculo com o valor delas
troco = valor_pago - total

print(f"seu preço total e de {total} e seu troco e de {troco}")#devolve em sua tela com o calcuo feito