import tkinter as tk
import random

placa_correta = ""
mostrar_resposta_flag = False
mercosul_mode = False  # Variável para controlar o modo Mercosul
recorde = 0  # Variável para armazenar o recorde do jogador

def calcular_pontuacao(tempo, placas):
    if mercosul_mode:
        return int(tempo) * int(placas) * 1.5 * 100
    else:
        return int(tempo) * int(placas) * 100

def gerar_placa():
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "0123456789"
    if mercosul_mode:
        placa = ""
        for i in range(3):
            placa += random.choice(letras)
        placa += random.choice(numeros)
        placa += random.choice(letras)
        for i in range(2):
            placa += random.choice(numeros)
    else:
        placa = ""
        for i in range(3):
            placa += random.choice(letras)
        for i in range(4):
            placa += random.choice(numeros)
    return placa

def mostrar_placa_mercosul():
    global placa_correta, mostrar_resposta_flag
    placa_correta = gerar_placa()
    mostrar_resposta_flag = False
    mostrar_placa_window = tk.Toplevel(root)
    mostrar_placa_window.geometry("325x100")
    mostrar_placa_window.title("Placa Mercosul" if mercosul_mode else "Placa Clássica")
    mostrar_placa_window.configure(bg="white")  # Define o fundo como branco
    if mercosul_mode:
        # Adicione a faixa azul na parte superior
        faixa_azul = tk.Frame(mostrar_placa_window, bg="blue", height=20)
        faixa_azul.pack(fill="x")
        texto_brasil = tk.Label(faixa_azul, text="Brasil", font=("Times", 12, "bold"), bg="blue", fg="white")
        texto_brasil.place(relx=0.5, rely=0.5, anchor="center")
    label = tk.Label(mostrar_placa_window, text=placa_correta, font=("Fixedsys", 50), bg="white")
    label.pack(expand=True)
    mostrar_placa_window.after(5000, lambda: mostrar_resposta(mostrar_placa_window))  # Intervalo de 5 segundos

def mostrar_resposta(janela_anterior):
    global mostrar_resposta_flag
    mostrar_resposta_flag = True
    resposta_window = tk.Toplevel(root)
    resposta_window.title("Resposta")
    resposta_window.geometry("314x160")  # Aumentando a altura para acomodar o botão "Quit"
    resposta_window.config(bg="#1c1c33")
    resposta_label = tk.Label(resposta_window, text="Digite a placa:", font=("Times", 16))
    resposta_label.pack(pady=10)
    resposta_label.config(bg="#1c1c33")
    resposta_label.config(fg="#dedede")
    resposta_entry = tk.Entry(resposta_window, font=("Times", 16), width=10, justify="center")
    resposta_entry.pack()
    resposta_entry.config(bg="#dedede")
    resultado_label = tk.Label(resposta_window, font=("Times", 12, "bold"), bg="#1c1c33")
    resultado_label.pack(pady=10)
    
    def verificar_resposta(event):
        global recorde
        resposta = resposta_entry.get()
        if resposta.upper().replace("-", "") == placa_correta.upper().replace("-", ""):
            resultado_label.config(text="Correto!", fg="green")
            placas = 1  # Uma placa correta foi feita
        else:
            resultado_label.config(text=f"Incorreto! Placa correta: {placa_correta}", fg="red")
            placas = 0

        pontuacao = calcular_pontuacao(5, placas)  # Exemplo de tempo (5 segundos)

        if pontuacao > recorde:
            recorde = pontuacao
            recorde_label.config(text=f"Recorde: {recorde}")

        resposta_window.after(2000, resposta_window.destroy)  # Fecha a janela de resposta após 2 segundos.
        root.after(2000, mostrar_placa_mercosul)  # Chama mostrar_placa para reiniciar o jogo após 2 segundos.
    
    resposta_entry.bind("<Return>", verificar_resposta)
    
    # Botão "Quit" para encerrar a rodada do jogo
    quit_button = tk.Button(resposta_window, text="Quit", font=("Times", 12), command=resposta_window.destroy)
    quit_button.config(bg="red", fg="#ffffff")
    quit_button.pack(pady=5)

    janela_anterior.destroy()

def atualizar_modo():
    global mercosul_mode
    mercosul_mode = not mercosul_mode  # Inverte o valor do modo

def sair_do_jogo():
    root.quit()

root = tk.Tk()
root.geometry("250x300")  # Ajustando o tamanho da janela
root.config(bg="#1c1c33")
root.title("MindPlate")

# Redesign do menu inicial
titulo_label = tk.Label(root, text="MindPlate", font=("Times", 25), bg="#1c1c33", fg="#d6c800")
titulo_label.pack(pady=10)

descricao_label = tk.Label(root, text="O novo jogo da memória!", font=("Times", 14), bg="#1c1c33", fg="#dedede")
descricao_label.pack()

modo_var = tk.StringVar()

# Recorde em negrito acima do modo de placa
recorde_label = tk.Label(root, text=f"Recorde: {recorde}", font=("Times", 15, "bold"), bg="#1c1c33", fg="#dedede")
recorde_label.pack(pady=10)

modo_label = tk.Label(root, text="Modo de Placa:", font=("Times", 16), bg="#1c1c33", fg="#dedede")
modo_label.pack(pady=10)

modo_frame = tk.Frame(root, bg="#1c1c33")
modo_frame.pack()

modo_mercosul = tk.Radiobutton(modo_frame, text="Mercosul", font=("Times", 14), variable=modo_var, value="Mercosul", command=atualizar_modo)
modo_mercosul.config(bg="#1c1c33", fg="white", selectcolor="#1c1c33")
modo_mercosul.pack(side="left")

modo_classica = tk.Radiobutton(modo_frame, text="Clássica", font=("Times", 14), variable=modo_var, value="Clássica", command=atualizar_modo)
modo_classica.config(bg="#1c1c33", fg="white", selectcolor="#1c1c33")
modo_classica.pack(side="right")

botoes_frame = tk.Frame(root, bg="#1c1c33")
botoes_frame.pack()

iniciar_botao = tk.Button(botoes_frame, text="Iniciar", font=("Times", 16), command=mostrar_placa_mercosul)
iniciar_botao.config(bg="#d6c800", fg="#ffffff")
iniciar_botao.pack(side="left", padx=10)

sair_botao = tk.Button(botoes_frame, text="Sair", font=("Times", 16), command=sair_do_jogo)
sair_botao.config(bg="red", fg="#ffffff")
sair_botao.pack(side="right", padx=10)

root.mainloop()
