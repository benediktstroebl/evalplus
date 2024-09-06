def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'

    # Make sure the first and last character are not consonants
    if word[0] in consonants and word[-1] in consonants:
        word = word[1:-1]

    # Count index of right-most consonant on the right side of the word
    conc_idx = -1
    for i, each_char in enumerate(word):
        if each_char in consonants:
            conc_idx = i
            break

    # Find the closest vowel to the right of the right-most consonant
    for i, each_char in enumerate(word[conc_idx+1:], start=conc_idx+1):
        if each_char in vowels:
            return each_char

    return ""