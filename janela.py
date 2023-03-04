import os
import tkinter as tk 
from tkinter import font
from tkinter import messagebox

# cria a janela principal
janela = tk.Tk()
#Titulo da Janela
janela.title('Hinário - Senador Hélio Campos 2023')
# Define o tamanho da janela
janela.geometry("500x200")
# desabilitando a opção de maximizar a janela
janela.resizable(False, False)
# função que é chamada quando o botão é clicado
def open_video():
    # obtém o nome do arquivo digitado pelo usuário
    video_name = entry.get()  
    filename ="{video_name}.mp4"
    if video_name == "":
         messagebox.showerror('Atenção', 'Digite um Hino')
    elif os.path.isfile(filename):
        messagebox.showerror('Atenção', 'Hino Não Encontrado')       
    else:
        # executa o comando no terminal para abrir o arquivo no player padrão
        os.system(f'xdg-open "{video_name}.mp4"')
        video_name = entry.get()
        #Apagar texto apos o click
        entry.delete(0, tk.END)

#Variavel de fontes
fontes = font.Font(family='Roboto', size=12, weight='bold')
    
# cria a entrada de texto e o botão os componentes da tela
label1 = tk.Label(janela, text='HINÁRIO',)
label1.pack()
label2 = tk.Label(janela, text='Adventista do Sétimo Dia')
label2.pack()
#Cria Input
entry = tk.Entry(janela)
entry.pack(side='top', pady='10')
button = tk.Button(janela, text='Tocar Hino', command=open_video)
button.pack()
#Configuração de componetes
janela.config(background='#fff')
label1.config(background='#fff', fg='#E6AA00', font='fontes')
label2.config(background='#fff', fg='#E6AA00', font='fontes')
entry.config(justify='right', font='fontes')
button.config(background='#E6AA00', bd='0', activebackground='#fff', fg='#fff', font='fontes') 




janela.mainloop()
