# Passo a passo do projeto
# ---------------------------------------------------------------
# 1. Abrir o sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# para instalar: pp install pyautogui
import pyautogui
from time import sleep

pyautogui.PAUSE = 0.5
# pyautogui.click -> para clicar com o mouse
# pyautogui.write -> para escrever um texto
# pyautogui.press -> para pressionar uma tecla do teclado
# pyautogui.hotkey -> apertar um conjunto de teclas (Ctrl C, Ctrl V, Alt Tab, etc.)

# Abrir o navegador (Chrome)
pyautogui.press('win')
pyautogui.write('Chrome')
pyautogui.press('enter')

# Entrar no site do sistema

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# Aqui pode ser que ele demora alguns segundos para carregar o site
sleep(2)

# 2. Fazer login
pyautogui.click(x=665, y=413)
pyautogui.write('teste123@gmail.com')

pyautogui.press('tab') # passou para o campo de senha
pyautogui.write('123abc')

pyautogui.press('tab') # passou para o botão de login
pyautogui.press('enter')

# 3. Abrir/Importar a base de dados de produtos para cadastrar
# pip install pandas numpy openpyx1
import pandas as pd

tabela = pd.read_csv('produtos.csv')

# 4. Cadastrar um produto
for linha in tabela.index:
    # clicar no campo do codigo do produto
    pyautogui.click(x=413, y=293, clicks=2)

    # codigo
    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    # passar para o próximo
    pyautogui.press('tab')

    # marca
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    # passar para o próximo
    pyautogui.press('tab')

    # tipo
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    # passar para o próximo
    pyautogui.press('tab')

    # categoria
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    # passar para o próximo
    pyautogui.press('tab')

    # preço
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    # passar para o próximo
    pyautogui.press('tab')

    # custo
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    # passar para o próximo
    pyautogui.press('tab')

    # obs
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    # passar para o próximo
    pyautogui.press('tab')

    # apertar o botão
    pyautogui.press('enter')
    # voltar ao topo
    pyautogui.scroll(5000)

# 5. Repitir isso tudo até acabar a lista de produtos

