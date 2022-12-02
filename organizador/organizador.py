"""
Projeto Final
Requisito: Crie pastas e mova os arquivos para dentro delas, com base nas suas
extensões.
Autor: Keilon Reckers Ferreira
Versão 0.0.1
"""

# Importando pacotes

import os
import shutil

# Criando pastas

def pastas(x, y):
    x = "Planilhas"
    y = "Documentos"
    if(not os.path.exists(pasta_planilhas)):
        os.mkdir(pasta_planilhas)
    if(not os.path.exists(pasta_documentos)):
        os.mkdir(pasta_documentos)

# Movendo os arquivos em pastas com a mesma extensão

def main():
    pasta = os.getcwd()
    for arquivo in pasta:
        if "xlsx" in arquivo:
            shutil.move(f"organizador/{arquivo}", 'pasta_planilhas/')
        if "docx" in arquivo:
            shutil.move(f"organizador/{arquivo}", 'pasta_documentos/')

# Execução da função principal

if __name__ == "__main__":
    main()

                



        
