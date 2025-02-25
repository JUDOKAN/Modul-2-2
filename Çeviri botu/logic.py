from collections import defaultdict
from translate import Translator

class TextAnalysis:
    # Görev #1 - Mesajları saklamak için defaultdict kullanımı
    memory = defaultdict(list)

    # Görev #5 - Kullanıcının mesajlarına yanıtları içeren sözlük
    questions = {
        'adın ne?': "Ben süper havalı bir botum ve amacım size yardım etmek!",
        "kaç yaşındasın?": "Bu çok felsefi bir soru..."
    }

    def __init__(self, text, owner):
        self.text = text
        self.owner = owner

        # Görev #2 - Memory sözlüğüne yeni bir anahtar-değer çifti ekleme
        TextAnalysis.memory[owner].append(self)

        # Görev #6 - Kullanıcının mesajının sözlükte olup olmadığını kontrol etme
        if self.text.lower() in TextAnalysis.questions.keys():
            self.response = TextAnalysis.questions[self.text.lower()]
        else:
            self.translation = self.__translate(self.text, "tr", "en")
            self.response = self.get_answer()

    def get_answer(self):
        translated_text = self.__translate("I don't know how to help", "en", "tr")
        return translated_text

    def __translate(self, text, from_lang, to_lang):
        try:
            # Görev #3 - translate kütüphanesini kullanarak çeviri yapmak
            translator = Translator(from_lang=from_lang, to_lang=to_lang)
            translation = translator.translate(text)
            return translation
        except Exception as e:
            return f"Çeviri girişimi başarısız oldu: {str(e)}"
