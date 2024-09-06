def get_closest_vowel(word):
    """
    Find the closest vowel to the right of consonant sequences within a word.
    
    Args:
        word (str): The input word.
    
    Returns:
        str: The closest vowel to the right of consonant sequences, or an empty string if none is found.
    """
    vowels = 'AEIOUaeiou'
    len_word = len(word)
    for i in range(len_word):
        if word[i] in vowels and word[i] != word[len_word - 1]:
            right_side = word[i + 1:len_word]
            if any(c in consonants for consonants in consonant_sequences for c in right_side):
                return word[i]
        elif word[i] == word[len_word - 1]:
            break
    return ''