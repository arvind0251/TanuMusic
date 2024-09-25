from pyrogram import Client, filters
from gtts import gTTS
from TanuMusic import app


@app.on_message(filters.command('tts'))
def text_to_speech(client, message):
    text = message.text.split(' ', 1)[1]
    tts = gTTS(text=text, lang='hi')
    tts.save('tanu.mp3')
    client.send_audio(message.chat.id, 'tanu.mp3')
  
