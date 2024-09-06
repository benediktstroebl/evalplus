def get_closest_vowel(word):
    """
    Find the closest vowel to the right of consonant sequences in a string.
    
    Args:
        word (str): Input string.

    Returns:
        str: The closest vowel to the right of consonant sequences or an empty string.
    """
    vowels = 'AEIOUaeiou'
    len_word = len(word)
    for i in range(len_word):
        if word[i] in vowels:
            if i > 0 and word[i-1] in consonants:
                return word[i]
        elif word[i] in consonants:
            if i < len_word - 1 and word[i+1] in vowels:
                return word[i+1]
    return ''