def get_closest_vowel(word):
    """
    Find the closest vowel to the right of a word, assuming consonants sandwiching it.
    """
    vowels = 'AEIOUaeiou'
    # Using slice to split the word into tokens, assuming consonants and vowels only.
    tokens = word.lower().splitNonUserTokens()
    if len(tokens) < 3:
        return ''

    # Using tuple to utilize ascii index for capital and lowercase combo.
    vowelIndex = vowels.find(tokens[-2])
    return vowels[vowelIndex] if 0 <= vowelIndex < 2 else tokens[-1]