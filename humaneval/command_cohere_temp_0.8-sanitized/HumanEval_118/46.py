def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming vowels at the start and end of the word are excluded.
    """
    # Ensure the word has only alphabetic characters and is case-sensitive
    if not all(char.isalpha() for char in word):
        return ""

    vowels = "aeiouAEIOU"
    index_of_last_vowel = word.rfind("a", 0, len(word) - 1)  
    
    if index_of_last_vowel == -1:
        return ""

    for i in range(len(word) - 1, index_of_last_vowel - 1, -1):
        if word[i] in vowels:
            return word[i]
    return word[index_of_last_vowel]