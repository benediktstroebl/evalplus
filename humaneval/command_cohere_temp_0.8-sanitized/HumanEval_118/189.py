def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming the vowels occur between two consonants.
    Empty string if no qualifying vowel is found.
    """
    # Ensure the word has at least 2 characters to avoid edge cases
    if len(word) < 2:
        return ""

    # Ensure the first and last character are not vowels
    if word[0].lower() in 'aeiou':
        word = word[1:]
    if word[-1].lower() in 'aeiou':
        word = word[:-1]

    # Iterate through characters in the word
    for i, char in enumerate(word):
        if char.lower() in 'aeiou':
            # Check if the character to the right is a consonant
            if i < len(word) - 1 and word[i+1].isalpha() and word[i+1].lower() not in 'aeiou':
                return char
        else:
            continue

    # If no qualifying vowel is found, return an empty string
    return ""