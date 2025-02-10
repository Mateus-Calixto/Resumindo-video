#importação das bibliotecas

from openai import OpenAI

import pytubefix
import ffmpeg
import whisper


#configuração da chave de api
cliente = OpenAI(api_key="sua api_key", base_url="https://api.deepseek.com")
#baixar video
def baixar_video(url):
    yt = pytubefix.YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    caminho_arquivo = video.download(filename="audio.mp4")
    return caminho_arquivo

def extrair_audio(caminho_video):
    caminho_audio = "audio.wav"
    ffmpeg.input(caminho_video).output(caminho_audio, format='wav', acodec='pcm_s16le', ac=1, ar='16000').run(overwrite_output=True, quiet=True)
    return caminho_audio


def transcrever_audio(audio_path):
    """Transcreve o áudio usando Whisper"""
    model = whisper.load_model("small")
    result = model.transcribe(audio_path)
    return result["text"]


def resumir_texto(texto):

    response = cliente.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": f"Resuma o seguinte texto: {texto}"}],
    stream=False
)

    print(response.choices[0].message.content)




def main():


    print("Ola tudo bem?")

    while True:

        url = input("Digite a Url do video que deseja resumir")
        if url.find('?') != -1:  #encontrando qualquer posição válida
           #baixar video
           print("🔽 Baixando vídeo...")
           video_path = baixar_video(url)
           


           print("🎵 Extraindo áudio...")
           caminho_audio = extrair_audio(video_path)
           
           print("📝 Transcrevendo áudio...")
           texto = transcrever_audio(caminho_audio)

           print("✍️ Gerando resumo...")
           resumo = resumir_texto(url)

           print("\n📄 Resumo gerado:\n")
           print(resumo)

        else:
            print("URL inválida.")
         





if __name__ == "__main__":
    main()