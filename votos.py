voto1 = input("Você quer: PLAYSTATION, XBOX ou NITENDO?")
voto2 = input("Você quer: PLAYSTATION, XBOX ou NITENDO?")
voto3 = input("Você quer: PLAYSTATION, XBOX ou NITENDO?")
voto4 = input("Você quer: PLAYSTATION, XBOX ou NITENDO?")
voto5 = input("Você quer: PLAYSTATION, XBOX ou NITENDO?")

playstation = 0
xbox = 0
nitendo = 0

lista = [voto1, voto2, voto3, voto4, voto5]
for voto in lista:
  if voto.upper() == "PLAYSTATION":
    playstation += 1
  elif voto.upper() == "XBOX":
    xbox += 1
  elif voto.upper() == "NITENDO":
    nitendo += 1
  else:
    print("O colaborador digitou um console inexistente e seu voto será desconsiderado.")

if playstation > xbox and playstation > nitendo:
  print("O console escolhido foi o playstation")
elif xbox > playstation and xbox > nitendo:
  print("O console escolhido foi o xbox")
elif nitendo > xbox and nitendo > playstation:
  print("O console escolhido foi o nitendo")
else:
  print("Houve empate")

print("PLAYSTATION: {}\nXBOX: {}\nNITENDO: {}".format(playstation, xbox, nitendo))
