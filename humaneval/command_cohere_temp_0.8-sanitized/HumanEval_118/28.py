def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming the vowels occur between two consonants.
    Ignores vowels at the start and end of the word.
    """
    vowels = 'AEIOUaeiou'
    # Removing vowels at the start and end
    trimmed = word.strip(word.lower())
    # If the word is empty now, no vowels to find
    if not trimmed:
        return ''
    # Find the index of the last consonant
    last_consonant_idx = len(trimmed) - 1
    while last_consonant_idx > 0 and trimmed[last_consonant_idx].lower() in vowels:
        last_consonant_idx -= 1
    # Find the closest vowel after that consonant (going back or passing it)
    for i in range(last_consonant_idx + 1, len(trimmed)):
        if trimmed[i].lower() in vowels:
            return trimmed[i]
    # No vowel after the last consonant, so we must have a single consonant
    # We return the very last character (original word's last character)
    return word[-1]