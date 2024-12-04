import yt_dlp
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def download_youtube_video():
    url = url_entry.get()
    save_path = path_entry.get()

    if not url or not save_path:
        messagebox.showwarning("Input Error", "Por favor, insira a URL do vídeo e o diretório de destino.")
        return

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    ydl_opts = {
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            messagebox.showinfo("Download Completo", "O vídeo foi baixado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro ao Baixar", f"Erro ao baixar o vídeo: {e}")

def browse_directory():
    folder_selected = filedialog.askdirectory()
    path_entry.delete(0, tk.END)
    path_entry.insert(0, folder_selected)

# Configurar a janela principal
root = tk.Tk()
root.title("YouTube Video Downloader by Gabriel Yan ")

# Configurar a interface
tk.Label(root, text="URL do Vídeo do YouTube:").grid(row=0, column=0, padx=10, pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Diretório de Destino:").grid(row=1, column=0, padx=10, pady=10)
path_entry = tk.Entry(root, width=50)
path_entry.grid(row=1, column=1, padx=10, pady=10)

browse_button = tk.Button(root, text="Procurar", command=browse_directory)
browse_button.grid(row=1, column=2, padx=10, pady=10)

download_button = tk.Button(root, text="Baixar", command=download_youtube_video)
download_button.grid(row=2, column=1, padx=10, pady=10)

# Iniciar o loop da interface
root.mainloop()
