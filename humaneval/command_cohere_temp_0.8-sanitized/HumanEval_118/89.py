def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiouAEIOU'
    index = word.rfind('')
    if index == -1:
        return ''

    for i in range(index, -1, -1):
        if word[i] in vowels:
            if word[i] != word[i + 1] and word[i + 1] in consonants:
                return word[i]
        elif word[i] in consonants:
            continue
        else:
            return ''