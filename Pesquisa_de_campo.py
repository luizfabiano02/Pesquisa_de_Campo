print("********************************")
print("     PESQUISA DE SATISFAÇÃO")
print("********************************")

# Variáveis para armazenar a quantidade de respostas
excelente = 0
bom = 0
ruim = 0

#INICIANDO O LAÇO DE REPETIÇÃO - VERIFICAR POR QUAL MOTIVO ESTA DANDO 49 E NÃO 50
for i in range(1, 5): #NÃO HÁ NECESSIDADE DE COLOCAR CHAVES O PROGRMA JÁ INTERPRETA OS A ESCALA
#TESTAR CO 10, PARA VERIFICA SE O LAÇO ESTÁ FUNCIONANDO CORRETAMENTE, POIS O PROGRAMA NÃO ESTÁ PEGANDO 50 ENTREVISTADOS, E SIM 49
    print("\n*** Entrevistado", i, "***")

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("\nQual a sua opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite o número da opção: "))

    #INICIANDO OIF - PRECISEI DE AJUDA COM O CHATGPT PARA FAZER ESSA PARTE, POIS NÃO CONSEGUI FAZER SOZINHO
    if opiniao == 1: # deu erro quando o "=" ficou próximo do valor
        excelente = excelente + 1 #O alinhamento, o programa faz com que o mesmo não contabilize a quantidade de respostas BOM, e sim apenas EXCELENTE e RUIM, por isso precisei de ajuda do chatgpt para fazer essa parte

    elif opiniao == 2:
        bom = bom + 1

    elif opiniao == 3:
        ruim = ruim + 1

    else:
        print("Opção inválida!")
# REALIZER A TROCA POR OUTRO LAÇO OU MESMO O FOR, PARA QUE O PROGRAMA NÃO PARE CASO O USUÁRIO DIGITE UMA OPÇÃO INVÁLIDA, POIS O PROGRAMA ESTÁ PARANDO E NÃO CONTINUANDO A PESQUISA
# Resultado final
print("\n===========================+====")
print("     RESULTADO DA PESQUISA    ")
print("================================")
print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas RUIM:", ruim)
#print("Quantidade de respostas BOM:", bom) - colocado para testar se o programa está funcionando corretamente, pois o mesmo não estava contabilizando a quantidade de respostas BOM, e sim apenas EXCELENTE e RUIM