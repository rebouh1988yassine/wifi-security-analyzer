from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.utils import platform

if platform == "android":
    from jnius import autoclass
    from android.permissions import request_permissions
    from android.permissions import Permission


class WiFiAnalyzerApp(App):

    def build(self):
        self.layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        self.title_label = Label(
            text="WiFi Security Analyzer",
            font_size=24
        )

        self.result_label = Label(
            text="Press Scan to find nearby WiFi networks",
            font_size=16
        )

        self.scan_button = Button(
            text="Scan WiFi Networks",
            size_hint=(1, 0.2)
        )

        self.scan_button.bind(
            on_press=self.scan_wifi
        )

        self.layout.add_widget(self.title_label)
        self.layout.add_widget(self.result_label)
        self.layout.add_widget(self.scan_button)

        return self.layout

    def scan_wifi(self, instance):

        if platform != "android":
            self.result_label.text = (
                "WiFi scanning requires Android"
            )
            return

        self.result_label.text = "Scanning..."

        try:
            request_permissions([
                Permission.ACCESS_FINE_LOCATION,
                Permission.ACCESS_COARSE_LOCATION,
                Permission.ACCESS_WIFI_STATE,
                Permission.CHANGE_WIFI_STATE
            ])

            PythonActivity = autoclass(
                "org.kivy.android.PythonActivity"
            )

            Context = autoclass(
                "android.content.Context"
            )

            activity = PythonActivity.mActivity

            wifi = activity.getSystemService(
                Context.WIFI_SERVICE
            )

            wifi.startScan()

            networks = wifi.getScanResults()

            result = ""

            for network in networks:
                result += (
                    str(network.SSID)
                    + " | "
                    + str(network.BSSID)
                    + " | "
                    + str(network.level)
                    + " dBm\n"
                )

            if result:
                self.result_label.text = result
            else:
                self.result_label.text = (
                    "No networks found"
                )

        except Exception as e:
            self.result_label.text = str(e)


if __name__ == "__main__":
    WiFiAnalyzerApp().run()
