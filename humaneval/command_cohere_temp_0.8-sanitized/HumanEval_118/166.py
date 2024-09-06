def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming consonants sandwiching it.
    Ignores starting and ending vowels.
    """
    # Convert to lowercase for consistency and to ignore case
    word = word.lower()
    # Split the word on vowels to find general vowel positions and remove them
    # This also ensures starting and ending vowels are ignored
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = [c for c in word if c not in vowels]
    # If the word is empty, return an empty string immediately
    if not word:
        return ''
    # Split the word on spaces to get lists of consonants that may be sandwiched
    # between two consonants
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    vowel_positions = [i for i, char in enumerate(word) if char in vowels]
    sandwiched_consonants = [
        consonants[i:] + [consonants[i + 1]]
        for i, char in enumerate(word)
        if char in consonants
        and ((i and vowel_positions[i - 1] < vowel_positions[i]) or
             (i + 1 < len(word) and vowel_positions[i + 1] < vowel_positions[i + 2]))
    ]
    # Return the closest vowel to the right of the word, preferring uppercase
    if sandwiched_consonants:
        return vowels[0].upper() if vowels[0].isupper() else vowels[0]
    return ''