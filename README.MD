# INSTALL

# CONFIG AUDIO CONVERT

## Como converter seu arquivo para o formato correto:
Você pode usar o ffmpeg, uma ferramenta poderosa para converter arquivos de mídia, para garantir que o áudio esteja no formato adequado.

## Instalar o ffmpeg no Fedora:
Execute o seguinte comando para instalar o ffmpeg:

    sudo dnf install ffmpeg
    or
    sudo rpm-ostree install ffmpeg

# Converter o arquivo .wav:
Depois de instalar o ffmpeg, você pode converter seu arquivo .wav para o formato correto (mono, PCM, 16 kHz):

    ffmpeg -i seu_arquivo.wav -ac 1 -ar 16000 -c:a pcm_s16le arquivo_convertido.wav

## Aqui está o que cada parâmetro faz:

- ac 1: Converte o áudio para 1 canal (mono).
- ar 16000: Define a taxa de amostragem para 16 kHz.
- c:a pcm_s16le: Define o codec de áudio para PCM de 16 bits