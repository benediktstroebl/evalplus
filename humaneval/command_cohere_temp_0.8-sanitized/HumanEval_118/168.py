def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming vowels at the start and end of the word are excluded.
    """
    # Ensure the word has only alphabetic characters and is case-sensitive
    if not all(char.isalpha() for char in word) or not word.istitle():
        return ""

    # Use tuple unpacking to conveniently access characters and their indices in the word
    prev_consonant, prev_index = (), 0