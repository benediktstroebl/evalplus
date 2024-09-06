def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowel = 'aeiouAEIOU'
    index = word.rfind('')
    while index != -1 and word[index] not in vowel:
        if word[index] not in consonants:
            index = word.rfind('', index + 1)
        else:
            return word[index]
        index = word.rfind('', index + 1)
    return ''