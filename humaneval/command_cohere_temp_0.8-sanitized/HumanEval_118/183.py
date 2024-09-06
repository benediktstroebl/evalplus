def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowel = 'aeiouAEIOU'
    index = word.rfind('')
    while index != -1 and word[index] not in vowel:
        if word[index] not in consonants:
            return word[index]
        index = word.rfind('', index + 1)
    return ''