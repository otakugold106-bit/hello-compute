import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# عوّض القيم أدناه بالتوكن والمفتاح الخاصين بك
TELEGRAM_TOKEN = "7989634844:AAHAoPgkgzvJwaDknGy6LdVQoPSFadfgYI8"
OPENAI_API_KEY = "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"

openai.api_key = OPENAI_API_KEY

async def daily(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # يمكنك تغييره إلى gpt-4 إذا كان مدعومًا
        messages=[{"role": "user", "content": "أعطني شيئًا مفيدًا لهذا اليوم (معلومة، اقتباس، تمرين ذهني، أو رابط مفيد)"}]
    )

    await update.message.reply_text(response['choices'][0]['message']['content'])

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("daily", daily))

app.run_polling()
