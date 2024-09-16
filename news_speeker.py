from openai import OpenAI

import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)

class NEWS_SPEEKER:
    
    def __init__(self,openai_key,
                 behaviour_file_path,
                 vocal_tone,
                 audio_save_path) -> None:
        
        self.client = OpenAI(api_key=openai_key)

        with open(behaviour_file_path,'r') as file:
            content = file.read()

        self.ai_character = content
        self.vocal_tone = vocal_tone
        self.audio_save_path = audio_save_path


    def NewsToSpeech(self,news):
        completion = self.client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=1,
        messages=[
            {"role": "system", "content": self.ai_character},
            {
                "role": "user",
                "content": news
            }
            ]
            )
        
        return completion.choices[0].message.content
    

    def NewsToVocal(self,news):
        vocal = self.client.audio.speech.create(
        model="tts-1",
        voice=self.vocal_tone,
        input=self.NewsToSpeech(news),
        )

        vocal.stream_to_file(self.audio_save_path)


if __name__ == "__main__":

    # your openai_key
    key = ''

    # your output audio file path
    audio_save_path = ''

    speeker = NEWS_SPEEKER(
                        openai_key=key,
                        behaviour_file_path='behaviour.txt',
                        vocal_tone='onyx',
                        audio_save_path=audio_save_path
                        )

    # put you news here
    news=''

    
    speeker.NewsToVocal(news)