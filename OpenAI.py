import openai
from openai import RateLimitError, OpenAIError

client = openai.OpenAI(
    api_key=""
)

def get_completion(prompt, model="gpt-3.5-turbo"):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )
        return response.choices[0].message.content
    except RateLimitError:
        return "❌ Error: Rate limit exceeded or insufficient quota. Please check your OpenAI billing/usage."
    except OpenAIError as e:
        return f"❌ Error: {str(e)}"

# 🔹 Text to summarize
text = """
You should express what you want a model to do by \
providing instruction that are as clear and \
specific as you can possibly make them. \
This will guide the model towards the desired output, \
and reduce the chances of receiving irrelevent \
or incorrect responses. Don't confuse writing a \
clear prompt with writing a short prompt. \
In many cases, longer prompts provide more clarity \
and context for the model, which can lead to \
more detailed and relevant outputs.
"""

# 🔹 Prompt construction
prompt = f"""
Summarize the text delimited by triple backticks \
into a single sentence.
```{text}```
"""

# 🔹 Get and print the response
response = get_completion(prompt)
print(response)