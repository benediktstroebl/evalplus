def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiouAEIOU'
    word = word.lower()
    index = next((i for i, char in enumerate(word) if char in consonants), len(word))
    if index == 0 or index == len(word) or word[index - 1:] == 'ea' or word[index + 1:] == 'ea':
        return ''
    else:
        return word[index].upper() if word[index] in vowels else ''