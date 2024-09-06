def get_closest_vowel(word):
    vowels = 'AEIOUaeiou'
    consonants = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
    word = word.upper()
    
    if word[0] in consonants and word[-1] in consonants:
        for i in range(1, len(word) - 1):
            if word[i] in vowels:
                return word[i]
        else:
            return ''
    else:
        return ''