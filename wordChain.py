import re
from random import shuffle
import time
import os
import pymorphy2

Dificulty = 50                     # sum of games
with open('text.txt', "r") as file_in:
    text_raw = file_in.read()

text = [i for i in re.split(r'[\W]', text_raw) if len(i) > 3 and len(i) < 10]
shuffle(text)


def convert_text(word):
    result = ''
    dic = {'і': 'ы','h': 'р',' ': ' ','a': 'ф', 'm': 'ь', 'x': 'ч', 'i': 'ш',
        'f': 'а', '.': 'ю', 'n': 'т', 'k': 'л', ';': 'ж', 'u': 'г', '[': 'х',
        'y': 'н', 'd': 'в', ']': 'ъ', "'": 'э', 'w': 'ц', 'p': 'з', 'q': 'й', 
        'r': 'к', 'z': 'я', 'e': 'у', 't': 'е', 'v': 'м', 'l': 'д', 'o': 'щ', 
        'b': 'и', 'c': 'с', 's': 'ы', 'j': 'о', ',': 'б', 'g': 'п'}
    for letter in word:
        try:
            result += dic[letter]
        except:
            result += letter
    return result


def fetch_last_letter(user_word):
    if(user_word[-1] == 'э' or user_word[-1] == 'ь' or user_word[-1] == 'ы'):
        return user_word[-2]
    return user_word[-1]
    

def main():
    file_out = open('text1.txt', "w")
    words_in_game = []
    last_letter = ''
    games_was = 0
    morph = pymorphy2.MorphAnalyzer()
    print('Напиши "Выход" что бы выйти')
    while(True):
        user_word = convert_text(input("Введите слово: ").lower())
        if(user_word == 'выход'):
            break
    
        if(not morph.word_is_known(user_word)):
            print("Это вообще слово?!")
            continue
        
        if(user_word[0] != last_letter and games_was):
            print("Жулик! Ваше слово должно быть на последнюю букву моего слова!")
            continue
        
        if(user_word in words_in_game):
            print("Вы уже называли это слово!")
            continue
        
        file_out.write(user_word+'\n')
        last_letter = fetch_last_letter(user_word)
        words_in_game.append(user_word)
    
        if(games_was == Dificulty):
            time.sleep(3)
            print('Я не знаю больше слов... Вы победили')
    
        for word in text:
            if(last_letter == word[0] and not word in words_in_game):
                print("Мое слово: ")
                time.sleep(0.3)
                print(word)
                last_letter = fetch_last_letter(word)
                words_in_game.append(word)
                break
        games_was += 1
    
    print('Всего было слов: ', len(words_in_game))
    
    file_out.close()
    file_in = open("text1.txt", "r")
    file_out = open("text.txt", "a")
    for line in file_in.readlines():
        if(line not in text):
            file_out.write(line)
    
    file_in.close()
    file_out.close()

if __name__ == '__main__':
    main() 
    os.remove('text1.txt')  
