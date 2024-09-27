import os
import wave
import json
import vosk

# Função para abrir e processar o arquivo de áudio
def transcrever_audio(arquivo_wav, arquivo_saida, modelo_vosk="model"):
    # Carregar o modelo Vosk (deve ser baixado antes)
    if not os.path.exists(modelo_vosk):
        print(f"Modelo não encontrado em {modelo_vosk}. Por favor, baixe-o antes de continuar.")
        return

    # Inicializar o reconhecimento com o modelo especificado
    modelo = vosk.Model(modelo_vosk)

    # Abrir o arquivo de áudio
    wf = wave.open(arquivo_wav, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print("Este arquivo de áudio não está no formato suportado. Precisa ser um arquivo WAV mono PCM.")
        return

    reconhecedor = vosk.KaldiRecognizer(modelo, wf.getframerate())

    # Processar o áudio e realizar a transcrição
    transcricao = []
    while True:
        dados = wf.readframes(4000)
        if len(dados) == 0:
            break
        if reconhecedor.AcceptWaveform(dados):
            resultado = json.loads(reconhecedor.Result())
            transcricao.append(resultado['text'])

    # Adicionar o último resultado parcial
    resultado_final = json.loads(reconhecedor.FinalResult())
    transcricao.append(resultado_final['text'])

    # Salvar a transcrição em um arquivo de texto
    with open(arquivo_saida, 'w') as f:
        transcricao_completa = ' '.join(transcricao)
        f.write(transcricao_completa)

    print(f"Transcrição salva em {arquivo_saida}")

# Exemplo de uso
arquivo_wav = "audio.wav"  # Substitua pelo caminho do seu arquivo
arquivo_saida = "transcricao.txt"           # Nome do arquivo de saída
transcrever_audio(arquivo_wav, arquivo_saida)
