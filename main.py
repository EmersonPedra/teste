from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.uix.screenmanager import ScreenManager, Screen

Window.clearcolor = [1, 1, 1, 1]


class Gerenciador(ScreenManager):
    pass


class BotaoInicio(ButtonBehavior, Label):
    def __init__(self, **kwargs):
        super(BotaoInicio, self).__init__(**kwargs)
        self.atualizar()
        self.color = 0, 0, 0, 1
        self.font_size = 30

    def on_pos(self, *args):
        self.atualizar()

    def on_size(self, *args):
        self.atualizar()

    def atualizar(self):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=(0.5529, 0.760, 1, 1))
            Ellipse(size=self.size,pos=self.pos,source="imagem.png")




class BotaoConfirma(ButtonBehavior, Label):
    def __init__(self, **kwargs):
        super(BotaoConfirma, self).__init__(**kwargs)
        self.atualizar()
        self.color = .2627, .4235, .6117, 1
        self.font_size = 30

    def on_pos(self, *args):
        self.atualizar()

    def on_size(self, *args):
        self.atualizar()

    def atualizar(self):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=(0.5529, 0.760, 1, 1))
            Rectangle(size=(self.width/2, self.height/2),
                      pos=(self.center_x - self.width/4, self.center_y - self.height/4))
            Ellipse(size=(self.height/2, self.height/2),
                    pos=(self.center_x - self.width / 4 - self.height/4, self.center_y - self.height/4))
            Ellipse(size=(self.height/2, self.height/2),
                    pos=(self.center_x + self.width/4 - self.height/4, self.center_y - self.height/4))

            Color(rgba=(1, 1, 1, 1))
            Rectangle(size=(self.width / 2 - 4, self.height / 2 - 4),
                      pos=(self.center_x - self.width / 4 + 2, self.center_y - self.height / 4 + 2))
            Ellipse(size=(self.height / 2 - 4, self.height / 2 - 4),
                    pos=(self.center_x - self.width / 4 - self.height / 4 + 2, self.center_y - self.height / 4 + 2))
            Ellipse(size=(self.height / 2 - 4, self.height / 2 - 4),
                    pos=(self.center_x + self.width / 4 - self.height / 4 + 2, self.center_y - self.height / 4 + 2))


class Login(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class EntradaDeTexto(TextInput):
    def __init__(self, **kwargs):
        super(EntradaDeTexto, self).__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)
        self.cursor_color = (0.5529, 0.760, 1, 1)
        self.font_size = 30
        self.background_color = (1, 1, 1, 0)
        self.cursor_blink = True
        self.atualizar()

    def on_pos(self, *args):
        self.atualizar()

    def on_size(self, *args):
        self.atualizar()

    def atualizar(self):
        self.canvas.after.clear()
        with self.canvas.after:
            Color(rgba=(0.5529, 0.760, 1, 1))
            Rectangle(size=(self.width - 100, 5), pos=(self.center_x - self.width/2, self.y -5))



class Senha(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class TelaLogin(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Tabelas(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Tela1(App):
    def build(self):
        return Gerenciador()


Tela1().run()
