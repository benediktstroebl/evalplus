def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming consonants sandwiching the vowel
    """
    vowels = 'AEIOUaeiou'
    # Remove starting and ending vowels
    word = word.strip('AEIOUaeiou').strip('AEIOUaeiou')
    if len(word) < 2:
        return ''
    for i in range(1, len(word) - 1):
        if word[i] in vowels:
            if word[i - 1] in consonants and word[i + 1] in consonants:
                return word[i]
    return ''
consonants = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'