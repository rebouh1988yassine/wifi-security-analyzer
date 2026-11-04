
[app]

title = WiFi Security Analyzer

package.name = wifisecurityanalyzer

package.domain = org.rebouh

source.dir = .

source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy,pyjnius

orientation = portrait

fullscreen = 0

android.permissions = INTERNET,ACCESS_WIFI_STATE,CHANGE_WIFI_STATE,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION

android.api = 35

android.minapi = 23

android.ndk = 27b

android.archs = arm64-v8a

android.accept_sdk_license = True

[buildozer]

log_level = 2

warn_on_root = 1
