import pyautogui
import pandas
import time

# Abrindo Chrome
pyautogui.PAUSE = 0.3
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# link do formulário
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# preenchendo formulário login
pyautogui.click(x=735, y=373)
pyautogui.write("emailfake@email.com")
pyautogui.press("tab")
pyautogui.write("senhafake")
pyautogui.click(x=965, y=532)

# verificando tabela produtos.csv
tabela = pandas.read_csv("produtos.csv")
# print(tabela)


# Preenchendo produtos
for linha in tabela.index:
  pyautogui.click(x=743, y=256)

  pyautogui.write(tabela.loc[linha, "codigo"])
  pyautogui.press("tab")

  pyautogui.write(tabela.loc[linha, "marca"])
  pyautogui.press("tab")

  pyautogui.write(tabela.loc[linha, "tipo"])
  pyautogui.press("tab")

  pyautogui.write(str(tabela.loc[linha, "categoria"]))
  pyautogui.press("tab")

  pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
  pyautogui.press("tab")

  pyautogui.write(str(tabela.loc[linha, "custo"]))
  pyautogui.press("tab")

  obs = tabela.loc[linha, "obs"]
  if pandas.isna(obs):
    pyautogui.write(obs)
    pyautogui.press("tab")
    
  pyautogui.press("tab")
  pyautogui.press('enter')

  pyautogui.screenshot(5000)
