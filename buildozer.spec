[app]

# (str) Título de tu aplicación
title = MiAppPydroid

# (str) Nombre del paquete
package.name = miapptest

# (str) Dominio del paquete (puedes dejar este)
package.domain = org.test

# (str) Directorio donde está el main.py
source.dir = .

# (list) Extensiones de archivos a incluir
source.include_exts = py,png,jpg,kv,atlas

# (list) Requerimientos de la aplicación
# IMPORTANTE: Si usas KivyMD añade ",kivymd" al final sin espacios
requirements = python3,kivy==2.3.0

# (str) Orientación de la pantalla
orientation = portrait

# (bool) Indicar si la aplicación debe ser a pantalla completa
fullscreen = 1

# =================================================
# CONFIGURACIÓN DE ANDROID (CRÍTICO)
# =================================================

# (int) API de Android que se usará (33 es el estándar actual)
android.api = 33

# (int) Mínimo API soportado (Android 5.0)
android.minapi = 21

# (str) Versión del NDK de Android
android.ndk = 25b

# (bool) Aceptar licencias automáticamente (Evita el Error 100)
android.accept_sdk_license = True

# (str) Arquitectura (arm64-v8a es para celulares modernos)
android.archs = arm64-v8a

# (str) Formato de salida
android.release_artifact = apk

# (bool) Ocultar la barra de estado
android.skip_update = False

# =================================================
# CONFIGURACIÓN DE BUILDOZER
# =================================================

[buildozer]

# (int) Nivel de log (2 para ver errores detallados)
log_level = 2

# (int) Tiempo de espera antes de error
warn_on_root = 1

# (str) Rama de python-for-android a usar
p4a.branch = master
