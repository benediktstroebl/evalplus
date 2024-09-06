def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'
    # Finding possible vowels
    possible_vowels = []
    i = len(word) - 2
    while i >= 0 and word[i] not in consonants:
        if word[i] in vowels:
            possible_vowels.append(word[i])
        i -= 1
    # Checking if the possible vowels are between two consonants
    if len(possible_vowels) == 0:
        return ''
    for vowel in possible_vowels:
        if (word[i] in consonants and word[i + 1] in consonants and
                vowel in vowels):
            return vowel
    return ''