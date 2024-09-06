def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming the vowels occur between two consonants.
    Ignores starting and ending vowels.
    """
    vowels = 'AEIOUaeiou'  
    # Ensure casing is considered
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

    index = next((i for i, char in enumerate(word, 1) if char in consonants), None)
    while index < len(word):
        char = word[index]
        if char in vowels:
            if index == 0 or word[index-1] in consonants:
                return char.upper() if word[index].isupper() else char
            index += 1
        else:
            index += 1
            if index < len(word) and word[index] in consonants:
                index += 1
            else:
                break
    return ''