def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiouAEIOU'
    # Count the leading and trailing consonants
    leading, trailing = 0, 0
    for char in word:
        if char in consonants: leading = max(leading, 1)
        if char in vowels: trailing = max(trailing, 1)
    # Find the closest vowel in the middle
    for i, char in enumerate(word):
        if char in consonants and i > leading + trailing:
            if char in vowels: return char
        elif char in vowels:
            break
    return ''