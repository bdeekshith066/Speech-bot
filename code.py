!pip install openai==0.27.0 gtts
!pip install openai gtts pydub
!apt-get install -y python3-pyaudio
!pip install SpeechRecognition


from gtts import gTTS
from IPython.display import Audio, display
import openai
# Set your OpenAI API key
openai.api_key = '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'
def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    return response['choices'][0]['message']['content'].strip()
def text_to_speech(text):
    tts = gTTS(text, lang='en')
    tts.save("output.mp3")
    display(Audio("output.mp3", autoplay=True))
while True:
    # Prompt user for input
    user_input = input("How can I assist you today? ")
    # Generate response using ChatGPT
    chatgpt_response = generate_response(user_input)
    # Convert text response to speech and play it
    text_to_speech(chatgpt_response)
    # Ask for input again or break the loop
    user_choice = input("Do you want to ask something else? (yes/no) ").lower()
    if user_choice != 'yes':
        break
