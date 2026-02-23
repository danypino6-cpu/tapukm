[app]
title = MiAppGestion
package.name = gestionapp
package.domain = org.tuusuario
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db,csv
# REQUERIMIENTOS CORREGIDOS PARA TU CÓDIGO:
requirements = requirements = python3,kivy==2.3.0,kivymd==1.1.1,sdl2_ttf==2.0.15,sqlite3,csv

orientation = portrait
fullscreen = 1

# AJUSTES DE ANDROID
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True
android.release_artifact = apk

[buildozer]
log_level = 2
p4a.branch = master
