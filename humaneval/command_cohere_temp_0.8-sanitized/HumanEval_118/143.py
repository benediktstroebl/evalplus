def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowel = 'aeiouAEIOU'
    index = word.rfind("", 0, len(word) - 1)
    while index != -1 and word[index] not in vowel:
        if word[index] not in consonants:
            return ''
        index = word.rfind("", 0, index - 1)
    if index != -1 and word[index] in vowel:
        return word[index]
    return ''