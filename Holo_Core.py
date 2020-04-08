import pyautogui
from Azure_Voice_Output import Azure_Output

# pyautogui.hotkey("Ctrl", "T")
# pyautogui.typewrite("Teste")
# pyautogui.typewrite(["enter"])

def novaaba():
     pyautogui.click(x=924, y=26)
     pyautogui.typewrite("Teste")
     pyautogui.typewrite(["enter"])

def abrirteams():
     pyautogui.click(x=599, y=1060)

def abrirchat():
     pyautogui.click(x=328, y=259)

def digitar():
     pyautogui.typewrite("Ola Nicolas, isso e um teste")

def localizador():
     Azure_Output()

#Metodo de sintetização do nome acerca do reconhecimento de face
def Azure_name_post():
    from Azure_Voice_Output import Azure_Output
    Azure_Output()

def Azure_sign_post():
    from Azure_Voice_Output import Azure_Output
    Azure_Output()


