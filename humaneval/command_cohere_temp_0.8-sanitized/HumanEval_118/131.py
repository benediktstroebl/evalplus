def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming consonants sandwiching it.
    """
    vowels = "AEIOUaeiou"
    # Remove starting and ending vowels:
    word = word.strip(vowels)
    if not word:
        return ""
    # Filter out all inner vowels:
    word = [c for c in word if c not in vowels]
    # Ensure there's at least one consonant left:
    if not word:
        return ""
    return next((c for c in word if c in vowels), "")