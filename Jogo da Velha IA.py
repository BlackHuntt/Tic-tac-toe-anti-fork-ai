placar = {"Samurai": 0, "Gananciosa": 0, "Empate": 0}

def mostrar_tabuleiro(tab):
    print(f"\n {tab[0]} | {tab[1]} | {tab[2]} ")
    print("----|----|----")
    print(f" {tab[3]} | {tab[4]} | {tab[5]} ")
    print("----|----|----")
    print(f" {tab[6]} | {tab[7]} | {tab[8]} ")

def verificar_vitoria(tab, jogador):
    if tab[0] == tab[1] == tab[2] == jogador: return True
    if tab[3] == tab[4] == tab[5] == jogador: return True
    if tab[6] == tab[7] == tab[8] == jogador: return True
    if tab[0] == tab[3] == tab[6] == jogador: return True
    if tab[1] == tab[4] == tab[7] == jogador: return True
    if tab[2] == tab[5] == tab[8] == jogador: return True
    if tab[0] == tab[4] == tab[8] == jogador: return True
    if tab[2] == tab[4] == tab[6] == jogador: return True
    return False

def verificar_empate(tab):
    return " " not in tab

def jogada_samurai_gananciosa(tabuleiro):
    for i in range(9):
        if tabuleiro[i] == " ":
            tabuleiro[i] = "O"
            if verificar_vitoria(tabuleiro, "O"):
                tabuleiro[i] = " "
                print(f" XEQUE MATE NA CASA {i}! JAERA BABY!")
                return i
            tabuleiro[i] = " "

    for i in range(9):
        if tabuleiro[i] == " ":
            tabuleiro[i] = "X"
            if verificar_vitoria(tabuleiro, "X"):
                tabuleiro[i] = " "
                print(f" HAHAH HJ NAO {i}! BLOQUEADO! TENTOU ME MATAR?")
                return i
            tabuleiro[i] = " "

    if tabuleiro[4] == "O":
        if tabuleiro[0] == "X" and tabuleiro[8] == "X":
            beiradas = [1, 3, 5, 7]
            for b in beiradas:
                if tabuleiro[b] == " ":
                    print(f" SAFADA! QUASE ME FEZ UM GARFO! PEGO BEIRADA {b}!")
                    return b
        if tabuleiro[2] == "X" and tabuleiro[6] == "X":
            beiradas = [1, 3, 5, 7]
            for b in beiradas:
                if tabuleiro[b] == " ":
                    print(f" SAFADA! QUASE ME FEZ UM GARFO! PEGO BEIRADA {b}!")
                    return b

    if tabuleiro[4] == " ":
        print(" GANANCIOSA: CENTRO É MEU! OURO PURO! ")
        return 4

    cantos = [0, 2, 6, 8]
    for canto in cantos:
        if tabuleiro[canto] == " ":
            print(f" CANTOOO {canto} é meu tbn HAHAH ")
            return canto

    beiradas = [1, 3, 5, 7]
    for beirada in beiradas:
        if tabuleiro[beirada] == " ":
            print(f" LIXOO vou pegar na casa {beirada}... que ódio ")
            return beirada

def jogar():
    global placar
    tabuleiro = [" "] * 9
    print("SAMURAI GANANCIOSA v1.0 ENTRO NO JOGO!")
    print("Voce é o X | GANANCIOSA é O ")

    while True:
        mostrar_tabuleiro(tabuleiro)

        while True:
            try:
                jogada = int(input("TUA Vez Samurai escolhe 0-8 "))
                if 0 <= jogada <= 8 and tabuleiro[jogada] == " ":
                    tabuleiro[jogada] = "X"
                    break
                else:
                    print("Casa Ocupada ou Invalida Presta atencao Jogador ")
            except:
                print("Digita Numero Abestado!")

        if verificar_vitoria(tabuleiro, "X"):
            mostrar_tabuleiro(tabuleiro)
            print("VOCE Venceu a Gananciosa?! IMPOSSIVEL!")
            placar["Samurai"] += 1
            break

        if verificar_empate(tabuleiro):
            mostrar_tabuleiro(tabuleiro)
            print("EMPATE! Ela Nao Gosta mas Aceita...")
            placar["Empate"] += 1
            break

        print("\nVez da Gananciosa pensando...")
        jogada_ia = jogada_samurai_gananciosa(tabuleiro)
        tabuleiro[jogada_ia] = "O"

        if verificar_vitoria(tabuleiro, "O"):
            mostrar_tabuleiro(tabuleiro)
            print("GANANCIOSA: JAERA BABY CENTRO E CANTO TUDO MEU PERDEU! HAHAHA")
            placar["Gananciosa"] += 1
            break
        if verificar_empate(tabuleiro):
            mostrar_tabuleiro(tabuleiro)
            print("EMPATE! Pelo menos nao peguei beirada!")
            placar["Empate"] += 1
            break

if __name__ == "__main__":
    while True:
        jogar()
        print(f"\nPLACAR ATUAL: Samurai {placar['Samurai']} x {placar['Gananciosa']} Gananciosa | Empates: {placar['Empate']}")
        denovo = input("Revanche? s/n: ")
        if denovo.lower()!= "s":
            print("FLW SAMURAI! PLACAR FINAL:")
            print(placar)
            break