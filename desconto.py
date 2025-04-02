# entrada dados
valor_bruto = float(input("Informe o valor bruto do pacote: "))
categoria = input(
    "Informe a categoria do assento: ECONOMICA, EXECUTIVA ou PRIMEIRA CLASSE ")
quantidade_viajantes = int(input("Informe a quantidade de viajantes: "))

valor_desconto = 0

if categoria.upper() == "ECONOMICA":
  if quantidade_viajantes == 2:
     valor_desconto = valor_bruto * 0.03
  elif quantidade_viajantes == 3:
     valor_desconto = valor_bruto * 0.04
  elif quantidade_viajantes >= 4:
     valor_desconto = valor_bruto * 0.05

  if categoria.upper() == "EXECUTIVA":
    if quantidade_viajantes == 2:
      valor_desconto = valor_bruto * 0.05
    elif quantidade_viajantes == 3:
      valor_desconto = valor_bruto * 0.07
    elif quantidade_viajantes >= 4:
      valor_desconto = valor_bruto * 0.08

  if categoria.upper() == "PRIMEIRA CLASSE":
    if quantidade_viajantes == 2:
      valor_desconto = valor_bruto * 0.1
    elif quantidade_viajantes == 3:
      valor_desconto = valor_bruto * 0.15
    elif quantidade_viajantes >= 4:
      valor_desconto = valor_bruto * 0.8

else:
    print("Categora inexistente, não será concedido nenhum desconto!")

valor_liquido = valor_bruto - valor_desconto
media_viajante = valor_liquido / quantidade_viajantes

print(
    "O valor da viagem é de R${}. Após os descontos de R${}, a viagem custará R${}. Cada passagem tem um custo médio de R${}".format(
        valor_bruto, valor_desconto, valor_liquido, media_viajante))
