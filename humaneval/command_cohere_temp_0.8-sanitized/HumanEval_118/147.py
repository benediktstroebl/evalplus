def get_closest_vowel(word):
    vowels = 'AEIOUaeiou'
    len_word = len(word)
    
    # Make sure the word isn't empty
    if len_word == 0:
        return ''

    # If the last character is a vowel, return it
    if word[-1] in vowels:
        return word[-1]

    # Check if the last consonant is surrounded by two vowels
    idx_consonant = len_word - 1
    while idx_consonant >= 0 and word[idx_consonant] not in vowels:
        idx_consonant -= 1

    # If such consonant exists and there's a vowel to the right of it, return that vowel
    if idx_consonant + 1 < len_word and word[idx_consonant + 1] in vowels:
        return word[idx_consonant + 1]

    # If no close vowels are found, return the very last character of the word (which is a consonant)
    return word[-1]