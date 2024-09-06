def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'
    # Count the first and last consonant from right side.
    cnt = (word[::-1].find(consonants) + 1) if word[-1] in consonants else 0
    # Count the first and last vowel from right side.
    vcnt = (word[::-1].find(vowels) + 1) if word[-1] in vowels else 0
    if vcnt >= 2 and cnt >= 1:
        return word[-vcnt-2:-vcnt-1]
    elif vcnt >= 1 and cnt == 0:
        return word[-vcnt-1:]
    else:
        return ''