#CALCULADORA DE CR


ciclo = 0

#AQUI VERIFICA SE O ALUNO É DO PRIMEIRO PERÍODO DA EMAP, SE NÃO FOR ELE SAI DO PROGRAMA E SE ELE DIGITAR ERRADO O PROGRAMA VOLTA

while ciclo == 0:
 
    periodo = input("Você é do primeiro periodo de algum curso da EMAP?(s/n) ")

    if periodo == "s":
        break
    elif periodo == "n":
        print ("Essa calculadora é apenas para os alunos do primeiro período da EMAP!")
        exit()
    else:
        print("Digite (s) para sim e (n) para não!")
        continue

#AQUI ELE COLETA AS NOTAS DOS ALUNOS POR DISCIPLINA E CALCULA O CR, CASO ELE NÃO SEJA DE CD OU MAT O PROGRAMA VOLTA PARA ELE DIGITAR CORRETAMENTE
while ciclo == 0:
    
    print("Digite exit para sair.")
    curso = input("Qual o seu curso?(mat/cd) ")

    if curso == "mat":
        notacalc = float(input("Digite sua nota em Cálculo em uma Variável: ").replace(",", "."))
        notafund = float(input("Digite sua nota em Fundamentos de Matemática: ").replace(",", "."))
        notageoa = float(input("Digite sua nota em Geometria Analítica: ").replace(",", "."))
        notaintcp = float(input("Digite sua nota em Introdução à Computação: ").replace(",", "."))
        notaintmm = float(input("Digite sua nota em Introdução à Modelagem Matemática: ").replace(",", "."))

        for discip in [notaintcp, notacalc, notafund, notageoa, notaintmm]:
            
            if discip > 10 or discip < 0:
                print("Tá de sacanagem? Tu tirou uma nota negativa ou maior que 10? Tente novamente!")
                exit()
            else:
                cr = (notaintcp * 9 + notacalc * 9 + notafund * 6 + notageoa * 6 + notaintmm * 6) / 36
        break
   
    elif curso == "cd":
        notacalc = float(input("Digite sua nota em Cálculo em uma Variável: ").replace(",", "."))
        notafund = float(input("Digite sua nota em Fundamentos de Matemática: ").replace(",", "."))
        notageoa = float(input("Digite sua nota em Geometria Analítica: ").replace(",", "."))
        notaintcp = float(input("Digite sua nota em Introdução à Computação: ").replace(",", "."))
        notaintcd = float(input("Digite sua nota em Introdução à Ciência de Dados: ").replace(",", "."))

        for discip in [notaintcp, notacalc, notafund, notageoa, notaintcd]:
            
            if discip > 10 or discip < 0:
                print("Tá de sacanagem? Tu tirou uma nota negativa ou maior que 10? Tente novamente!")
                exit()
            else:
                cr = (notaintcp * 9 + notacalc * 9 + notafund * 6 + notageoa * 6 + notaintcd * 6) / 36
        break
    elif curso == "exit":
        print("Você saiu!")
        exit()
    else:
        print("Digite (mat) para Matemática Aplicada e (cd) para Ciência de Dados e Inteligência Artificial!")
        continue

if cr < 7 and cr >= 0:
    print(f"Seu CR PARCIAL é {cr:.2f} CUIDADO!!!")
elif cr >= 7 and cr < 8.5:
    print(f"Seu CR PARCIAL é {cr:.2f} MUITO BEM!")
elif cr >= 8.5 and cr <= 10:
    print(f"Seu CR PARCIAL é {cr:.2f} PARABÉNS!!!")
else:
    print("Seu CR PARCIAL deu negativo ou maior que 10, isso não faz sentido, você provavelmente colocou algum dado incorreto!!!")

