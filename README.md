# TheFeel - Servidor de Feel The Snow con Tailscale

Este repositorio contiene todo lo necesario para configurar un servidor de Feel The Snow utilizando Tailscale.

## Archivos incluidos

- **fts_server.py**: Script principal que descarga la configuración de Tailscale desde GitHub Pages y luego lanza el juego.
- **tailscale_setup.sh**: Script de configuración que instala Tailscale y lo conecta utilizando la clave de autenticación.
- **tailscale.json**: Archivo JSON que contiene la URL pública de `tailscale_setup.sh`. Este archivo se sirve a través de GitHub Pages.
- **.gitignore**: Archivo generado automáticamente para evitar subir archivos temporales.

## Configuración

1. **Sube este repositorio a GitHub** con el nombre `thefeel` bajo el usuario `fedevijivani`.
2. **Configura GitHub Pages**:
   - Ve a la pestaña **Settings** del repositorio.
   - En la sección **Pages**, selecciona la rama `main` (o la que uses) y la carpeta raíz (`/ (root)`).
   - Obtendrás un URL público, el cual debería ser similar a:  
     `https://fedevijivani.github.io/thefeel/`
3. **Verifica el archivo JSON**:
   - Accede a `https://fedevijivani.github.io/thefeel/tailscale.json` y asegúrate de que muestra el contenido correcto.
4. **Coloca el ejecutable del juego** `FeelTheSnow.exe` en la carpeta raíz de tu máquina local (no lo subas a GitHub).
5. **Ejecuta el servidor**:
   - Abre una terminal en tu máquina o Codespace.
   - Ejecuta: `python3 fts_server.py`
   - El script descargará y ejecutará la configuración de Tailscale y luego lanzará el juego.

## Notas

- **No incluyas `FeelTheSnow.exe` en el repositorio** por temas de derechos de autor. Solo debe estar en la máquina local donde ejecutes el servidor.
- Asegúrate de que el comando en `tailscale_setup.sh` utiliza la opción correcta `--authkey`.

¡Disfruta de tu servidor de Feel The Snow con Tailscale!
