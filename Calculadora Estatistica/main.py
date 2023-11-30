import sqlite3
from tkinter import Tk, Label, Entry, Button, StringVar, font
from funcionalidades_CalcEstatistica import verificar_login, abrir_tela_cadastro


def main():
    caminho_banco_dados = r'C:\Users\kevin\OneDrive\Documentos\Calculadora Estatistica\repositorio_CalcEstatistica.db'
    conexao = sqlite3.connect(caminho_banco_dados)
    janela = Tk()
    janela.title("Autenticação")
    janela.geometry("300x150")

    fonte = font.Font(size=12)

    Label(janela, text="Login", font=fonte).grid(row=0, pady=5)
    Label(janela, text="Senha", font=fonte).grid(row=1, pady=5)

    usuario_var = StringVar()
    senha_var = StringVar()

    Entry(janela, textvariable=usuario_var, font=fonte, width=20).grid(row=0, column=1, padx=10, pady=5)
    Entry(janela, textvariable=senha_var, show='*', font=fonte, width=20).grid(row=1, column=1, padx=10, pady=5)

    Button(janela, text="Entrar", command=lambda: verificar_login(janela, conexao, usuario_var, senha_var), font=fonte).grid(row=2, column=0, pady=10)
    Button(janela, text="Cadastrar", command=lambda: abrir_tela_cadastro(janela, conexao, fonte, usuario_var, senha_var), font=fonte).grid(row=2, column=1, pady=10)

    janela.mainloop()

if __name__ == "__main__":
    main()
