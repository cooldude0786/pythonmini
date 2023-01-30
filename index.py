from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window

class FloatingButtonApp(App):
    def build(self):
        btn = Button(text='Floating Button',
                     size_hint=(None, None),
                     size=(150, 50))
        btn.bind(on_press=self.exit_app)
        return btn

    def on_start(self):
        Window.size = (150, 50)
        Window.top = 200
        Window.left = 200
        self.root.pos = (0, 0)

    def exit_app(self, *args):
        App.get_running_app().stop()

if __name__ == '__main__':
    FloatingButtonApp().run()
