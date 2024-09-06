def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiouAEIOU'
    index = len(word) - 1
    while index >= 0 and word[index] in consonants:
        index -= 1
    if index == -1:
        return ''
    vowel = word[index]
    if vowel in vowels:
        return vowel
    return get_closest_vowel(word[:index] + word[index + 1:])