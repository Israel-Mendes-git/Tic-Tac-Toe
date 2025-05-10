import tkinter
from tkinter import *
from tkinter import ttk

# cores
co0 = "#FFFFFF"  # branca / white
co1 = "#333333"  # preta pesado / dark black
co2 = "#fcc058"  # laranja / orange
co3 = "#38576b"  # valor / value
co4 = "#3297a8"   # azul / blue
co5 = "#fff873"   # amarela / yellow
co6 = "#fcc058"  # laranja / orange
co7 = "#e85151"   # vermelha / red
co8 = co4   # + verde
co10 ="#fcfbf7"
fundo = "#3b3b3b" # preta / black

# criando a janela principal 
janela = Tk()
janela.title('')
janela.geometry('260x400')  # altura ajustada
janela.configure(bg=fundo)

# Dividindo a janela em 2 frames 
frame_cima = Frame(janela, width=240, height=100, bg=co1, relief="raised")
frame_cima.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_baixo = Frame(janela, width=240, height=280, bg=fundo, relief="flat")  # altura reduzida
frame_baixo.grid(row=1, column=0, sticky=NW, padx=10, pady=0)

# configurando o frame cima 
app_x = Label(frame_cima, text='X', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co7)
app_x.place(x=25, y=10)
app_x = Label(frame_cima, text='Jogador 1', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0)
app_x.place(x=17, y=70)
app_x_pontos = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_x_pontos.place(x=80, y=20)

app_separador = Label(frame_cima, text=':', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_separador.place(x=110, y=20)

app_o = Label(frame_cima, text='O', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co4)
app_o.place(x=170, y=10)
app_o = Label(frame_cima, text='Jogador 2', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0)
app_o.place(x=165, y=70)
app_o_pontos = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_o_pontos.place(x=130, y=20)



# configurando o frame baixo com Canvas para desenhar o tabuleiro
canvas = Canvas(frame_baixo, width=240, height=320, bg=fundo, highlightthickness=0)
canvas.grid(row=0, column=0, pady=0)




#criando logica do app

jogador_1 = "X"
jogador_2 = "O"

score_1 = 0
score_2 = 0

tabela = [['1', '2', '3'], 
          ['4','5','6'], 
          ['7','8','9']]

jogando = 'X'
joga = '' 
contador = 0
contador_de_rodada = 0
app_vencedor = None



def iniciar_jogo():
    global b_0, b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_8
    global tabela, jogando, contador, score_1, score_2

    global b_jogar, app_vencedor

    contador_de_rodada = 0

    if b_jogar:
        b_jogar.destroy()
        b_jogar = None
    if app_vencedor:
        app_vencedor.destroy()
        app_vencedor = None

    # Deleta botão e mensagem, se existirem



    tabela = [['', '', ''], ['', '', ''], ['', '', '']]
    jogando = 'X'
    contador = 0


    # Limpa o canvas antes de redesenhar
    canvas.delete("all")

    # Desenha o tabuleiro
    canvas.create_line(80, 20, 80, 220, width=6, fill=co0)
    canvas.create_line(160, 20, 160, 220, width=6, fill=co0)
    canvas.create_line(20, 80, 220, 80, width=6, fill=co0)
    canvas.create_line(20, 160, 220, 160, width=6, fill=co0)


    def controlar(i):
        global jogando, contador

        botoes = [b_0, b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_8]
        mapa = {
            1: (0, 0),
            2: (0, 1),
            3: (0, 2),
            4: (1, 0),
            5: (1, 1),
            6: (1, 2),
            7: (2, 0),
            8: (2, 1),
            9: (2, 2),
        }

        i = int(i)
        linha, coluna = mapa[i]
        botao = botoes[i - 1]

        if botao['text'] == '':
            cor = co7 if jogando == 'X' else co8
            botao['fg'] = cor
            botao['text'] = jogando
            tabela[linha][coluna] = jogando
            contador += 1
            verificar_vencedor()
            jogando = 'O' if jogando == 'X' else 'X'

    def verificar_vencedor():
        global score_1, score_2, contador
        

        # Verifica linhas, colunas e diagonais
        for i in range(3):
            if tabela[i][0] == tabela[i][1] == tabela[i][2] != '':
                anunciar_vencedor(tabela[i][0])
                return
            if tabela[0][i] == tabela[1][i] == tabela[2][i] != '':
                anunciar_vencedor(tabela[0][i])
                return

        if tabela[0][0] == tabela[1][1] == tabela[2][2] != '':
            anunciar_vencedor(tabela[0][0])
            return
        if tabela[0][2] == tabela[1][1] == tabela[2][0] != '':
            anunciar_vencedor(tabela[0][2])
            return

        if contador == 9:
            anunciar_vencedor('Empate')

    def anunciar_vencedor(v):
        global app_vencedor, b_jogar, contador_de_rodada
        global score_1, score_2, jogando, contador

        for botao in [b_0, b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_8]:
            botao['state'] = 'disable'

        if v == 'X':
            score_1 += 1
            app_x_pontos['text'] = str(score_1)
            mensagem = 'O jogador 1 venceu !!!'
        elif v == 'O':
            score_2 += 1
            app_o_pontos['text'] = str(score_2)
            mensagem = 'O jogador 2 venceu !!!'
        else:
            mensagem = 'Foi um empate !!!'

        app_vencedor = Label(frame_baixo, text=mensagem, width=20,
                            relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2)
        app_vencedor.place(x=20, y=220)

        contador_de_rodada += 1

        if contador_de_rodada >= 5:
            terminar()
            return

        b_jogar = Button(frame_baixo, command=iniciar_jogo, text='Próxima rodada', width=15, height=1,
                        font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0)
        b_jogar.place(x=55, y=250)


    def terminar():
        global contador_de_rodada, app_vencedor, b_jogar, score_1, score_2

        for botao in [b_0, b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_8]:
            botao['state'] = 'disable'

        app_vencedor = Label(frame_baixo, text='Fim da partida (5 rodadas)', width=25,
                            relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2)
        app_vencedor.place(x=10, y=45)

        def jogar_denovo():
            global score_1, score_2, contador_de_rodada
            app_x_pontos['text'] = '0'
            app_o_pontos['text'] = '0'
            score_1 = 0
            score_2 = 0
            contador_de_rodada = 0
            if app_vencedor:
                app_vencedor.destroy()
            if b_jogar:
                b_jogar.destroy()
            iniciar_jogo()

        b_jogar = Button(frame_baixo, command=jogar_denovo, text='Jogar Novamente', width=15, height=1,
                        font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0)
        b_jogar.place(x=50, y=250)


            


    # Cria os botões
    b_0 = Button(frame_baixo, command=lambda: controlar(1), text='', width=3, height=1, font=('Ivy 22 bold'),
                 overrelief=RIDGE, relief='flat', bg=fundo, fg=co0)
    b_0.place(x=13, y=15)
    b_1 = Button(frame_baixo, command=lambda: controlar(2), text='', width=3, height=1, font=('Ivy 22 bold'),
                 overrelief=RIDGE, relief='flat', bg=fundo, fg=co0)
    b_1.place(x=88, y=15)
    b_2 = Button(frame_baixo, command=lambda: controlar(3), text='', width=3, height=1, font=('Ivy 22 bold'),
                 overrelief=RIDGE, relief='flat', bg=fundo, fg=co0)
    b_2.place(x=165, y=15)
    b_3 = Button(frame_baixo, command=lambda: controlar(4), text='', width=3, height=1, font=('Ivy 22 bold'),
                 overrelief=RIDGE, relief='flat', bg=fundo, fg=co0)
    b_3.place(x=13, y=90)
    b_4 = Button(frame_baixo, command=lambda: controlar(5), text='', width=3, height=1, font=('Ivy 22 bold'),
                 overrelief=RIDGE, relief='flat', bg=fundo, fg=co0)
    b_4.place(x=88, y=90)
    b_5 = Button(frame_baixo, command=lambda: controlar(6), text='', width=3, height=1, font=('Ivy 22 bold'),
                 overrelief=RIDGE, relief='flat', bg=fundo, fg=co0)
    b_5.place(x=165, y=90)
    b_6 = Button(frame_baixo, command=lambda: controlar(7), text='', width=3, height=1, font=('Ivy 22 bold'),
                 overrelief=RIDGE, relief='flat', bg=fundo, fg=co0)
    b_6.place(x=13, y=165)
    b_7 = Button(frame_baixo, command=lambda: controlar(8), text='', width=3, height=1, font=('Ivy 22 bold'),
                 overrelief=RIDGE, relief='flat', bg=fundo, fg=co0)
    b_7.place(x=88, y=165)
    b_8 = Button(frame_baixo, command=lambda: controlar(9), text='', width=3, height=1, font=('Ivy 22 bold'),
                 overrelief=RIDGE, relief='flat', bg=fundo, fg=co0)
    b_8.place(x=165, y=165)

# Botão Jogar posicionado mais acima
b_jogar = Button(frame_baixo, command=iniciar_jogo, text='Jogar', width=10, height=1, font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0)
b_jogar.place(x=77, y=250)


janela.mainloop()