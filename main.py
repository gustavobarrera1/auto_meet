import webbrowser as wb
import pyautogui as pyto  ## para instalarlo, escribe en la terminal "pip install pyautogui"


def run():

    url = ["https://meet.google.com/ngy-wjki-ejt?pli=1"]

    wb.register(
        "edge",
        None,
        wb.BackgroundBrowser(
            "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        ),
    )
    a = wb.get("edge")  # depende del navegador esto cambia
    a.open(url[0])

    pyto.sleep(7)  # espera el ingreso al navegador
    pyto.hotkey("F11")
    pyto.sleep(1)
    pyto.hotkey("ctrlleft", "d")  # desactivar camara
    pyto.hotkey("ctrlleft", "e")  # desactivar microfono
    pyto.sleep(1)
    pyto.click(1260, 540)  # depende de la resolucion esto cambia
    pyto.hotkey("F11")


if __name__ == "__main__":
    run()
