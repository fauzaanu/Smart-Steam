# unable to run after being packaged by pyinstaller

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.config import Config
from kivymd.uix.dialog import MDDialog
from main import the_main

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '500')

THROTTLE_VALIDATION = False


class MainApp(MDApp):
    title = 'Smart Steam v0.1.0'

    def __init__(self):
        super().__init__()

        self.dialog = MDDialog(
            text="Please fill in both the values first!",
        )


    def show_error(self):
        if self.root.ids.throttle_input.text == "":
            print("No text entered")
        # make sure that the text entered is a number
        elif self.root.ids.throttle_input.text.isnumeric():
            globals()["THROTTLE_VALIDATION"] = True
            pass
        else:
            self.root.ids.throttle_input.text = "Please enter a number Example: 100"
            self.root.ids.throttle_input.error = True
            self.root.ids.throttle_input.text = ""
        print("Error")

    def throttle_steam(self):
        # check the throttle speed
        # check the current button text
        # check the full speed

        throttle_speed = self.root.ids.throttle_input.text
        full_speed = self.root.ids.full_speed_input.text
        current_button_text = self.root.ids.action_button.text

        if full_speed == "" or throttle_speed == "":
            print("No text entered")
            self.dialog.open()
            return

        if current_button_text == "Throttle":
            self.root.ids.action_button.text = "De-Throttle"
            self.root.ids.status_label.text = "Steam has been throttled to " + throttle_speed + " kbps"
            print("Throttling Steam")
            the_main(int(throttle_speed), int(full_speed))
        else:
            self.root.ids.action_button.text = "Throttle"
            self.root.ids.status_label.text = str("Steam is at full network speed")
            print("de-throttling Steam")
            the_main(int(throttle_speed), int(full_speed), throttle=False)

        return 1

    def de_throttle_steam(self):
        # print(event)
        print("de-throttling Steam")
        self.root.ids.label.text = str("Steam is at full speed")
        return 1

    def build(self):
        self.icon = 'icon.png'
        _fixed_size = (425, 350)  # desired fix size
        Window.size = _fixed_size
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.accent_palette = "Red"

        def reSize(*args):
            Window.size = _fixed_size
            return True

        Window.bind(on_resize=reSize)


MainApp().run()
