def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowel = 'aeiouAEIOU'
    # O(n) time where n is the length of the word
    i = len(word) - 1
    while i >= 0:
        if word[i] in vowel:
            return word[i]
        if word[i] in consonants and i > 0 and word[i-1] in consonants:
            return vowel[0]
        i -= 1
    return ''