from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        button = Button(text = 'btn 1', font_size=30, on_release=self.incrementar)
        label = Label(text = 'label 1', font_size=30)
        box.add_widget(button)
        box.add_widget(label)
        return box

    def incrementar(self, button):
        button.text = 'soltei'
        

if __name__ == '__main__':
    MyApp().run()
