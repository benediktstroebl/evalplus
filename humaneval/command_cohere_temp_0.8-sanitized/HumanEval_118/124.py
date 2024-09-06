def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming consonants sandwiching the vowel.
    """
    vowels = 'IEOUaeiou' 
    len_word = len(word)

    # Ensure consonants sandwich the right vowel
    for i in range(1, len_word):
        if word[i] in vowels and (word[i-1] not in vowels or word[i+1] not in vowels):
            return word[i]

    return ''