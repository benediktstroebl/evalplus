def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming vowels at the start and end do not count.
    Empty string is returned if no such vowel exists.
    """
    # Ensure input is case-sensitive and only contains letters to avoid error
    cleaned_word = "".join(char for char in word if char.isalpha()).upper()
    
    # Use a dictionary to check if the rightmost character is a consonant (or the end) and move leftwards
    closest_vowel = ""
    for char in cleaned_word[::-1]:
        if char in "AEIOUaeiou":
            closest_vowel = char
            break
    cleaned_word = cleaned_word[:-len(closest_vowel)]
    
    # Ensure the closest vowel is between two consonants
    if cleaned_word.count("") == 1:
        return closest_vowel
    else:
        return ""