def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'
    # Omit the first and last character since they are easiest to fulfill
    for i in range(1, len(word) - 1):
        if word[i] in vowels and word[i-1] in consonants and word[i+1] in consonants:
            return word[i]
    return ''