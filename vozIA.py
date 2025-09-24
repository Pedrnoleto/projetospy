import pyttsx3
from kivy.app import App
from kivy.uix.button import Button

# Inicializa o motor de voz
ligar = pyttsx3.init()


class FalaApp(App):
    def build(self):
        btn = Button(text="Falar")
        btn.bind(on_press=self.falar)
        return btn

    def falar(self, instance):
        texto = "Kivy Kivy Kivy Kivy falando com você."
        ligar.say(texto)
        ligar.runAndWait()


FalaApp().run()
