import os
import asyncio
from deep_translator import GoogleTranslator
from tqdm import tqdm

# Clear the terminal
os.system('clear' if os.name == 'posix' else 'cls')

# List of languages to translate through
languages = [
    'af', 'sq', 'am', 'ar', 'hy', 'as', 'ay', 'az', 'bm', 'eu', 'be', 'bn', 
    'bho', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-CN', 'zh-TW', 'co', 'hr', 
    'cs', 'da', 'dv', 'doi', 'nl', 'en', 'eo', 'et', 'ee', 'tl', 'fi', 
    'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gn', 'gu', 'ht', 'ha', 'haw', 
    'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'ilo', 'id', 'ga', 'it', 'ja', 
    'jw', 'kn', 'kk', 'km', 'rw', 'gom', 'ko', 'kri', 'ku', 'ckb', 'ky', 
    'lo', 'la', 'lv', 'ln', 'lt', 'lg', 'lb', 'mk', 'mai', 'mg', 'ms', 
    'ml', 'mt', 'mi', 'mr', 'mni-Mtei', 'lus', 'mn', 'my', 'ne', 'no', 
    'or', 'om', 'ps', 'fa', 'pl', 'pt', 'pa', 'qu', 'ro', 'ru', 'sm', 
    'sa', 'gd', 'nso', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 
    'es', 'su', 'sw', 'sv', 'tg', 'ta', 'tt', 'te', 'th', 'ti', 'ts', 
    'tr', 'tk', 'ak', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 
    'yo', 'zu'
]

# Function to translate a word through multiple languages asynchronously
async def translate_word(word, iterations, master_bar):
    translated_text = word
    for i in range(iterations):
        with tqdm(total=len(languages), desc=f"Iteration {i+1}/{iterations}", leave=False, unit="language") as iteration_bar:
            for lang in languages:
                try:
                    # Perform the translation
                    translated_text = GoogleTranslator(source='auto', target=lang).translate(translated_text)
                    iteration_bar.update(1)  # Update iteration progress bar
                except Exception as e:
                    print(f"Translation Error for '{translated_text}' in {lang} --> {e}")
                    break
        master_bar.update(1)  # Update master progress bar after each iteration
    return translated_text

# Main async function to run translations for all words
async def main(words, iterations):
    with tqdm(total=len(words) * iterations, desc="Overall Progress", unit="iteration") as master_bar:
        tasks = [translate_word(word, iterations, master_bar) for word in words]
        results = await asyncio.gather(*tasks)
    return results

# Example usage - translating multiple words
words_to_translate = ["Hello my name is *censored*"]
timestotranslate = 3

# Run the async main function
if __name__ == "__main__":
    translations = asyncio.run(main(words_to_translate, timestotranslate))
    for word, translation in zip(words_to_translate, translations):
        print(f"Final Translation for '{word}': {translation}")
