nome = input("Qual o seu nome completo: ")
primeiro_nome = nome.split()[0]
print("Olá Sr(a), " + primeiro_nome + "! Seja bem-vindo(a)!")

while True:
    idade = input("Quantos anos você tem? ")
    if idade.isdigit():
        idade = int(idade)
        break
    else:
        print("Por favor, digite sua idade apenas em números.")

if idade >= 18:
    print("Que bacana você tem " + str(idade) +
          " anos, isso quer dizer que você é maior de idade e pode ingressar na empresa!")
else:
    print("Que pena você tem " + str(idade) +
          " anos, isso quer dizer que você é inapto para ingressar na empresa!")

ingressar = input(
    "Você deseja ingressar na empresa? Responda com Sim ou Não: ")

if ingressar.lower() == "sim":
    sim = True
    print("UHUU! Preencha abaixo as informações, queremos saber mais sobre você!")
else:
    sim = False
    print("Que pena! Esperamos vê-lo em outra oportunidade.")

if sim:
    experiencia = input(
        "Você possui experiência na área? Responda com Sim ou Não: ")
    if experiencia.lower() == "sim":
        print("Que ótimo! Sua experiência será um diferencial!")
    else:
        print("Não se preocupe, oferecemos treinamentos para nossos colaboradores.")


print("só você estiver vendo isso")
print("tome cuidado")
print("isso é um teste")
print("ele está olhando para você agora")
