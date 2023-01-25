# Текст на экране
from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self): # Создаем окно приложения
        # текст, экран, расположение на экране
        label = Label(text = 'Привет мир!', size_hint = (1,1),
                      pos_hint = {'center_x': .5, 'center_y': .5})
        return label






MainApp().run()