import pyautogui
import time
import pandas

# pyautogui.click -> clica
# pyautogui.write -> escreve um texto
# pyautogui.press -> aperta uma tecla
# pyautogui.hotkey -> aperta um atalho

pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Passo 1: Entrar no sistema da empresa
    # Abrir navegador
pyautogui.press("win") # apertar a tecla windows
pyautogui.write("Chrome") # digitar chrome
pyautogui.press("enter") # enter
    # Abrir site
pyautogui.write(link) # digitar link
pyautogui.press("enter") # enter
    # Fazer uma pausa maior para o site carregar
time.sleep(1.5)

# Passo 2: Fazer Login
    # Clicar no campo de email
pyautogui.click(x=718, y=413)
pyautogui.write("izabelliribeiros@gmail.com") # digitar email
pyautogui.press("tab") # ir para o próximo campo
pyautogui.write("chocolate") # digitar senha
pyautogui.press("tab") # ir para o próximo campo
pyautogui.press("enter") # enter
    # Fazer uma pausa maior para o site carregar
time.sleep(1.5)

# Passo 3: Abrir a base de dados (importar o arquivo)
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    # Passo 4: Cadastrar 1 produto
    pyautogui.click(x=860, y=290) # clicar no campo do código do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo)) # digitar o código do produto
    pyautogui.press("tab") # ir para o próximo campo

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preço
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs
    obs = tabela.loc[linha, "obs"]
    if obs != "nan":
        pyautogui.write(str(obs))
    pyautogui.press("tab") # passar para o botão enviar
    pyautogui.press("enter") # enviar cadastro  

    #passar para o início da tela
    pyautogui.scroll(5000)

# Passo 5: Repetir o passo 4 até acabar a lista de produtos