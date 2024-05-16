from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
from classes import MainWindow, IMTScreen, BodyArea, AlgoverScreen, BedDay, TempDisab
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivy.config import Config


class MyApp(MDApp):
    Config.set('kivy', 'exit_on_escape', 'False')
    back_button_press_counter = NumericProperty(0)

    def build(self):
        from kivy.base import EventLoop
        EventLoop.window.bind(on_keyboard=self.on_key)
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Orange'
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(MainWindow(name='main'))
        sm.add_widget(IMTScreen(name='IMT'))
        sm.add_widget(BodyArea(name='body_area'))
        sm.add_widget(AlgoverScreen(name='algover'))
        sm.add_widget(BedDay(name='bed_day'))
        sm.add_widget(TempDisab(name='temp_disab'))

        return sm

    def switch_active(self):
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )

    def on_key(self, window, key, *args):
        if key == 27:
            if app.root.current == 'main':
                if self.back_button_press_counter == 1:
                    self.stop()
                else:
                    Snackbar(text='Нажмите ещё раз, чтобы выйти', duration=.5).open()
                    self.back_button_press_counter += 1
                    Clock.schedule_once(self.reset_back_button_press_counter, 1.5)
            else:
                app.root.current = 'main'
        return True

    def reset_back_button_press_counter(self, *args):
        self.back_button_press_counter = 0


if __name__ == "__main__":
    app = MyApp()
    app.run()
