faturamento_anual = float(input("Por favor, informe seu faturamento anual: "))
tipo_assinatura = input("Informe o seu tipo de assinatura: \nBasic\nSilver\nGold\nPlatinum\n")

if tipo_assinatura.upper() == "BASIC":
  bonus = faturamento_anual * 0.3
elif tipo_assinatura.upper() == "SILVER":
  bonus = faturamento_anual * 0.2
elif tipo_assinatura.upper() == "GOLD":
  bonus = faturamento_anual * 0.1
elif tipo_assinatura.upper() == "PLATINUM":
  bonus = faturamento_anual * 0.05
else:
  bonus = 0
  print("Tipo de assinatura invalida")

print(f"Para um faturamento anual de {faturamento_anual} o bônus é de {bonus}")