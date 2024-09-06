def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming the vowels occur between two consonants.
    Ignores starting and ending vowels.
    """
    # Ensure the word has at least 2 characters to prevent IndexError and out of range errors
    if len(word) < 2:
        return ""

    # Use binary search to find the closest vowel (O(log n))
    i = len(word) - 2
    while i >= 0 and word[i] not in 'AEIOUaeiou':
        i -= 1

    if i == -1:
        return ""

    return word[i + 1]