import pyautogui
import pandas
import time


def tecla(tecla):
    teclapress = pyautogui.press(tecla)
    return teclapress


# Abrindo Chrome
pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# link do formulário
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

# preenchendo formulário login
pyautogui.click(x=735, y=373)
pyautogui.write("emailfake@email.com")
pyautogui.press("tab")
pyautogui.write("senhafake")
pyautogui.click(x=965, y=532)
time.sleep(10)

# verificando tabela produtos.csv
tabela = pandas.read_csv("produtos.csv")
# print(tabela)


# Preenchendo produtos
for linha in tabela.index:
  pyautogui.click(x=743, y=256)

  pyautogui.write("MOLO000251")
  pyautogui.press("tab")

  pyautogui.write("Logitech")
  pyautogui.press("tab")

  pyautogui.write("Mouse")
  pyautogui.press("tab")

  pyautogui.write("1")
  pyautogui.press("tab")

  pyautogui.write("25.95")
  pyautogui.press("tab")

  pyautogui.write("6.5 ")
  pyautogui.press("tab")

  pyautogui.write("")
  pyautogui.press("tab")

  pyautogui.press("tab")
  pyautogui.press('enter')

  pyautogui.screenshot(5000)

