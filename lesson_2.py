# Кнопка
from kivy.app import App
from kivy.uix.button import Button

class MainApp(App):
    def build(self): # Создаем окно приложения

        button = Button(text = 'Привет мир!')
        return button






MainApp().run()