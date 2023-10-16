# how to give shapes background images in kivy!
import random

from kivy.app import App
from kivy.graphics import Rectangle, Color, Ellipse
from kivy.uix.widget import Widget


class MainWidget(Widget):
    rect = None
    circle = None

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.init_shapes()

    def init_shapes(self):
        with self.canvas:
            self.rect = Rectangle(bg_color=Color(1, 1, 1))
            self.circle = Ellipse(bg_color=Color(1, 1, 1))
            self.rect.source = 'my_img.png'
            self.circle.source = 'my_img.png'

    def on_size(self, *args):
        self.rect.pos = (0, 0)
        self.rect.size = (int(self.width / 2), int(self.height / 2))
        self.circle.pos = (int(self.width / 2), int(self.height / 2))
        self.circle.size = (int(self.width / 3), int(self.height / 3))

    def on_touch_down(self, touch):
        if touch.pos[0] < self.width / 2 and touch.pos[1] < self.height / 2:
            self.canvas.clear()
            with self.canvas:
                color = Color(random.randint(0, 255) / 255,
                              random.randint(0, 255) / 255,
                              random.randint(0, 255) / 255)
                self.rect = Rectangle(bg_color=color)
                self.circle = Ellipse(bg_color=Color(1, 1, 1))
                self.rect.source = 'my_img.png'
                self.circle.source = 'my_img.png'
                '''self.rect.source = 'my_img.png'
                self.circle = Ellipse(bg_color=Color(1, 1, 1))
                self.circle.source = 'my_img.png' '''
                self.on_size()


class MyApp(App):
    pass


if __name__ == '__main__':
    MyApp().run()
