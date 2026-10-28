import os
import random


biblioteca_de_livros = []

def limpar_tela():
    os.system ("cls")

def menu_principal():
    print ("1) Adicionar novo livro ")
    print ("2) Ver livros ")
    print ("3) Sair da biblioteca ")

modelo_de_livro = {}

while True:
    
    limpar_tela()
    menu_principal()
    escolher_opcao = input("Escolha uma opção: ")
    
    if escolher_opcao == "1":
        limpar_tela()
        modelo_de_livro ["livro"] = input ("Qual o nome do livro? ")
        modelo_de_livro ["autor"] = input ("Qual o autor do livro: ")

        biblioteca_de_livros.append(modelo_de_livro.copy())

        print (f"Livro {modelo_de_livro["livro"]} adicionado com sucesso! ")
        input(" \nPressione qualquer tecla para voltar ao menu")
        
    elif escolher_opcao == "2":
        limpar_tela()
        print("--- LISTA DE LIVROS ---")
        gera_numero = random.randint(0, 5)
        for i, livro in enumerate (biblioteca_de_livros, 1):
            print(f"{i}. Livro: {livro["livro"]} | Autor: {livro["autor"]} | Quantidade: {gera_numero} ")
        input(" \nPressione qualquer tecla para voltar ao menu")
    
    elif escolher_opcao == "3":
        limpar_tela()
        print ("Saindo da biblioteca...")
        break
    
    else:
        limpar_tela()
        print ("Digíte apenas 1, 2 ou 3")
        input(" \nPressione qualquer tecla para voltar ao menu")
        