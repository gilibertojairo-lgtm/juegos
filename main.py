from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class HolaApp(App):
    def build(self):
        self.output = Label(text="Presiona el botón")
        hola_button = Button(text="Hola")
        hola_button.bind(on_press=self.say_hola)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.output)
        layout.add_widget(hola_button)
        return layout

    def say_hola(self, instance):
        self.output.text = "¡Hola! 👋"

if __name__ == "__main__":
    HolaApp().run()
