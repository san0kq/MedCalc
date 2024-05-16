from kivy.uix.screenmanager import Screen
from kivymd.uix.pickers import MDDatePicker


class MainWindow(Screen):

    def tab_calc(self):

        try:
            dose_for_day = float(self.ids.tab_dose_sub.text) * float(self.ids.tab_weight.text)
            tab_for_day = dose_for_day / float(self.ids.tab_amount_sub.text)
            tabl = tab_for_day / float(self.ids.tab_amount_taking.text)
            dose = tabl * float(self.ids.tab_amount_sub.text)
            self.ids.tab_result.text = f'Разовая доза: {"%.1f" % tabl} таб. или {"%.1f" % dose} мг.'

        except ValueError:
            self.ids.tab_result.text = f'Заполните все поля цифровыми значениями.'

    def susp_calc(self):

        try:
            dose_for_day = float(self.ids.susp_dose_sub.text) * float(self.ids.susp_weight.text)
            total_ml = dose_for_day * float(self.ids.susp_amount_ml.text) / float(self.ids.susp_amount_sub.text)
            dose = total_ml / float(self.ids.susp_amount_taking.text)
            total_day = total_ml * float(self.ids.susp_day_taking.text)

            self.ids.susp_result.text = f'Разовая доза: {"%.1f" % dose} мл.\nКоличество суспензии на весь курс: ' \
                                        f'{"%.1f" % total_day} мл.'
        except ValueError:
            self.ids.susp_result.text = f'Заполните все поля цифровыми значениями.'

    def switch_active(self):

        if self.ids.theme_style.text == 'Светлая тема':
            self.ids.theme_style.text = 'Тёмная тема'

        else:
            self.ids.theme_style.text = 'Светлая тема'


class IMTScreen(Screen):

    def imt_calc(self):

        try:
            result = float(self.ids.imt_weight.text) / (float(self.ids.imt_growth.text)**2)
            self.ids.imt_result.text = f'ИМТ = {"%.1f" % result}'

        except ValueError:
            pass

    def change(self):
        self.parent.current = 'body_area'


class BodyArea(Screen):

    def body_area_calc(self):

        try:
            result = (float(self.ids.body_area_weight.text) * float(self.ids.body_area_growth.text) / 3600) ** 0.5
            self.ids.body_area_result.text = f'ППТ = {"%.1f" % result} м²'

        except ValueError:
            pass


class AlgoverScreen(Screen):

    def algover_calc(self):

        try:
            result = float(self.ids.algover_hear_rate.text) / float(self.ids.algover_blood_pressure.text)
            self.ids.algover_result.text = f'ШИ Альговера = {"%.1f" % result}'

        except ValueError:
            pass


class BedDay(Screen):

    def on_save(self, instance, value, date_range):
        self.ids.bed_day_label.text = f'{str(len(date_range)-1)} койко-дней'

    def show_date_picker(self):
        date_picker = MDDatePicker(mode='range')
        date_picker.open()
        date_picker.bind(on_save=self.on_save)


class TempDisab(Screen):

    def on_save(self, instance, value, date_range):
        self.ids.temp_disab_label.text = f'{str(len(date_range))} дней ВН'

    def show_date_picker(self):
        date_picker = MDDatePicker(mode='range')
        date_picker.open()
        date_picker.bind(on_save=self.on_save)


