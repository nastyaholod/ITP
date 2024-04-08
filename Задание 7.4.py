#определяем тип предложения
def sentence_type(sentence):
    if "?" in sentence:
        return "вопросительное"
    elif "!" in sentence:
        return "восклицательное"
    else:
        return "повествовательное"

# Считываем текст из файла
with open("текст 7.4", "r", encoding='utf-8') as file:
    text = file.read()

# Разделяем текст на предложения
sentences = text.split(".")
sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

# Создаем словарь для хранения слов из повествовательных предложений
words = {}

# Проходим по предложениям и находим только повествовательные предложения
for sentence in sentences:
    if sentence_type(sentence) == "повествовательное":
        # Разделяем предложение на слова
        sentence_words = sentence.split()
        for word in sentence_words:
            # Убираем лишние символы и переводим в нижний регистр
            word = word.strip(".,?!").lower()
            # Добавляем слово в словарь
            words[word] = words.get(word, 0) + 1

# Выводим слова и их количество, которые встречаются только в повествовательных предложениях
for word, count in words.items():
    if count == 1:
        print(word, count)
    else:
        print(word, count)



