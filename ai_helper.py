import openai

client = openai.OpenAI(api_key="<YOUR-OPENAI-API-KEY>")

def explain_math(expression):
    prompt = f"Şu işlemi açıkla: '{expression}'. Adım adım göster. Negatif sayıları da anlat."

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sen bir matematik öğretmenisin."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI cevap veremedi: {e}"
