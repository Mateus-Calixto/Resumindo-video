# 🎥 Resumindo Vídeos do YouTube com OpenAI e FFmpeg

## 📌 Descrição
Este projeto permite baixar o áudio de um vídeo do YouTube, transcrevê-lo usando OpenAI Whisper e gerar um resumo do conteúdo utilizando a API da OpenAI.

## 🚀 Funcionalidades
- Baixar o áudio de um vídeo do YouTube utilizando `pytubefix`.
- Converter o áudio para um formato adequado usando `ffmpeg`.
- Transcrever o áudio em texto usando `OpenAI Whisper`.
- Resumir o texto utilizando `GPT-4` ou `GPT-3.5-turbo` da OpenAI.

## 🛠️ Tecnologias Utilizadas
- **Python**
- **pytubefix** (para download do vídeo)
- **ffmpeg** (para conversão de áudio)
- **OpenAI Whisper** (para transcrição do áudio)
- **OpenAI GPT-4/GPT-3.5-turbo** (para resumo do texto)

## 📦 Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/Resumindo-video.git
   cd Resumindo-video
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Certifique-se de ter o **ffmpeg** instalado no sistema:
   ```bash
   ffmpeg -version
   ```
   Se não estiver instalado, siga as instruções [aqui](https://ffmpeg.org/download.html).

5. Configure a chave da API da OpenAI:
   ```bash
   export OPENAI_API_KEY="sua-chave-aqui"  # Linux/macOS
   set OPENAI_API_KEY="sua-chave-aqui"     # Windows
   ```

## ▶️ Como Usar
1. Execute o script no terminal, passando a URL do vídeo como argumento:
   ```bash
   python app.py "https://www.youtube.com/watch?v=EXEMPLO"
   ```
2. O programa irá:
   - Baixar o áudio do vídeo
   - Converter para um formato adequado
   - Transcrever o áudio
   - Gerar um resumo com OpenAI
3. O resumo será exibido no terminal e salvo em um arquivo `resumo.txt`.

## 🔧 Possíveis Erros e Soluções
- **Erro: "The model `gpt-4` does not exist or you do not have access to it"**
  - Sua conta OpenAI pode não ter acesso ao `gpt-4`. Tente usar `gpt-4-turbo` ou `gpt-3.5-turbo`.

- **Erro: `ffmpeg` não encontrado**
  - Verifique se o `ffmpeg` está instalado e acessível no `PATH` do sistema.

- **Saída do `ffmpeg` aparecendo no terminal**
  - Use `quiet=True` na chamada do `ffmpeg-python` ou redirecione a saída para `os.devnull`.


## 📩 Contato
Caso tenha alguma dúvida ou sugestão, entre em contato pelo e-mail: **seuemail@example.com**.

