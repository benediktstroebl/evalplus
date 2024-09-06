def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiouAEIOU'
    word = word.lower()
    index = next((i for i, let in enumerate(word) if let in consonants), len(word))
    if index == 0 or index == len(word) or word[index - 1] in vowels and word[index + 1] in vowels:
        return ''
    return word[index]