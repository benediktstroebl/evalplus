def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'

    # Consider the last vowel met
    last_vowel = -1

    for i, char in enumerate(word):
        if char in vowels:
            if i > last_vowel + 1 and word[last_vowel + 1:i] in consonants:
                last_vowel = i

    return word[last_vowel] if last_vowel >= 0 else ''