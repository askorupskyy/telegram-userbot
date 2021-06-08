import os
from pyrogram import Client, filters
from gtts import gTTS


APP_ID = os.environ.get("APP_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")


if not (APP_ID and API_HASH):
    raise ValueError(
        "Telegram APP ID and API HASH were not found in .env file")


app = Client(api_id=APP_ID, api_hash=API_HASH,
             bot_token="", session_name="tg-audio-bot")


@app.on_message(filters.command("tts", prefixes="/") & filters.me)
def tts(client, msg):
    text = list(msg.text.split(" "))[1:]
    lang = "en"
    chat_id = msg.chat.id

    if "--delete" in text:
        msg.delete()
        text.remove("--delete")

    languages = list(filter(lambda c: "--lang" in c, text))
    if languages:
        lang = languages[-1].split("=")[1]
    for lan in languages:
        text.remove(lan)

    # convert back to text
    message = " ".join(text)
    # create a filename for the message
    filename = f'media/{message}-{lang}.ogg'
    # text-to-speech
    audio = gTTS(text=message, lang=lang, slow=False)
    audio.save(filename)
    # send audio
    client.send_voice(chat_id, filename)
    # delete the file
    os.remove(filename)


app.run()
