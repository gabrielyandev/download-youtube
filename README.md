# Baixador de Vídeos do YouTube com GUI

![Python](https://img.shields.io/badge/Python-3.12-blue.svg) ![GUI](https://img.shields.io/badge/GUI-Tkinter-green.svg) ![yt-dlp](https://img.shields.io/badge/Downloader-yt--dlp-red.svg) ![FFmpeg](https://img.shields.io/badge/FFmpeg-integrado-lightgrey.svg)
![Licença MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Este projeto é um aplicativo gráfico (GUI) intuitivo e fácil de usar, desenvolvido em Python, para baixar vídeos do YouTube. Ele permite que você insira a URL do vídeo e selecione o diretório de destino, baixando o conteúdo com a melhor qualidade disponível.

O aplicativo é distribuído como um **executável autônomo para Windows**, eliminando a necessidade de instalar Python ou quaisquer dependências adicionais no seu sistema. Basta baixar, executar e usar!

## ✨ Recursos

* **Interface Gráfica Intuitiva:** Desenvolvida com **Tkinter**, oferece uma experiência de usuário simples e descomplicada.
* **Melhor Qualidade de Vídeo e Áudio:** Utiliza a poderosa biblioteca `yt-dlp` para baixar automaticamente a melhor combinação de vídeo e áudio disponível para a URL fornecida.
* **Integração com FFmpeg:** O `yt-dlp` se integra perfeitamente ao `ffmpeg` (necessário no sistema) para combinar faixas de áudio e vídeo separadas, garantindo arquivos de saída completos e de alta qualidade.
* **Seleção de Diretório Fácil:** Permite ao usuário escolher convenientemente a pasta onde os vídeos serão salvos.
* **Portátil (Windows Executável):** Não requer instalação prévia de Python ou bibliotecas; basta executar o arquivo `.exe`.

## 🚀 Como Usar

### **Passo 1: Download do Aplicativo**

1.  Acesse o link abaixo para baixar a versão mais recente do aplicativo:
    [**>> FAÇA O DOWNLOAD AQUI <<**](https://github.com/gabrielyandev/download-youtube/archive/refs/heads/main.zip)

2.  Após o download, extraia todo o conteúdo do arquivo `main.zip` para uma pasta de sua preferência no seu computador.

### **Passo 2: Executando o Aplicativo**

* **No Windows:** Navegue até a pasta onde você extraiu os arquivos e clique duas vezes no arquivo `youtube_downloader_gui.exe` para iniciar o aplicativo.

### **Passo 3: Baixando o Vídeo**

1.  Na interface do aplicativo, cole a **URL completa** do vídeo do YouTube que deseja baixar no campo "URL do Vídeo do YouTube:".
2.  Clique no botão **"Procurar"** ao lado do campo "Diretório de Destino:" para escolher a pasta em seu computador onde o vídeo será salvo.
3.  Com a URL e o diretório de destino definidos, clique no botão **"Baixar"**.
4.  Aguarde o processo de download ser concluído. Uma mensagem de "Download Completo" será exibida quando o vídeo for salvo.

---
**Observação Importante:** Para que o download e a junção de áudio/vídeo funcionem corretamente (especialmente para as melhores qualidades), é fundamental que o **FFmpeg esteja instalado e configurado no PATH do seu sistema.** Se você encontrar erros de mesclagem, por favor, instale o FFmpeg. Uma maneira fácil de fazer isso é usando o Winget no PowerShell: `winget install FFmpeg.FFmpeg -e`
---

## 🛠️ Desenvolvimento (Para Contribuidores)

Se você deseja contribuir, auditar o código ou entender como o projeto foi desenvolvido:

* **Linguagem:** Python 3.12 (ou superior)
* **Bibliotecas Python Principais:**
    * `yt-dlp`: Para o download e processamento de vídeos do YouTube.
    * `tkinter`: Framework GUI nativo do Python.

    Você pode instalar essas dependências via pip:
    ```bash
    pip install yt-dlp
    ```
    (`tkinter` já vem com a instalação padrão do Python)

* **Geração do Executável:** O executável para Windows é gerado utilizando `PyInstaller`.
    ```bash
    pip install pyinstaller
    ```
    Um comando de exemplo para construir o executável (adaptado para o seu caso):
    ```bash
    pyinstaller --onefile --windowed --add-binary "C:\\path\\to\\ffmpeg\\bin;." youtube_downloader_gui.py
    ```
    * **`--onefile`**: Empacota tudo em um único executável.
    * **`--windowed`**: Evita que uma janela de console preta apareça.
    * **`--add-binary "C:\\path\\to\\ffmpeg\\bin;."`**: **Crucial!** Este argumento garante que o `ffmpeg.exe` (e `ffprobe.exe`) seja incluído no executável, caso você não queira depender da instalação do FFmpeg no sistema do usuário final. **Você precisará ajustar `C:\\path\\to\\ffmpeg\\bin` para o caminho real onde você tem o `ffmpeg.exe` e `ffprobe.exe` no seu ambiente de desenvolvimento.**
    * `youtube_downloader_gui.py`: O nome do seu script principal.

## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Para mais detalhes, consulte o arquivo [LICENSE](LICENSE) na raiz do repositório.

---