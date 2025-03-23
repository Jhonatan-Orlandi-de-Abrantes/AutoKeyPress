import time as t, keyboard as k

cond = False

def toggle(e):
    global cond

    cond = not cond
    print(f'Condicao = {cond}')

def teclas():
    while True:
        if cond:
            k.press('w')
            t.sleep(1)
            k.release('w')
    
            k.press('d')
            t.sleep(1)
            k.release('d')
    
            k.press('s')
            t.sleep(1)
            k.release('s')
    
            k.press('a')
            t.sleep(1)
            k.release('a')

k.on_press_key('F4', toggle)
teclas()