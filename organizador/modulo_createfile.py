"""
Módulo createfile.py
Requisito: Este módulo cria pastas no terminal.
Autor: Keilon Reckers Ferreira
Versão 0.0.1
"""

def pastas(x, y):
    x = "Planilhas"
    y = "Documentos"
    if(not os.path.exists(x)):
        os.mkdir(x)
    if(not os.path.exists(y)):
        os.mkdir(y)
