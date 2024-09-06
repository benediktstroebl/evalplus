def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming the vowels occur between two consonants.
    Ignores starting and ending vowels.
    """
    # Ensure the input is a string
    if not isinstance(word, str):
        raise TypeError("Input word should be a string")

    # Convert the string to lowercase to make the comparison case insensitive
    word = word.lower()

    # Split the word into individual characters to find the last vowel and the rightmost consonant
    vowels = ['a', 'e', 'i', 'o', 'u']
    last_vowel, rightmost_consonant = None, None
    for char in word:
        if char in vowels and (last_vowel is None or char != last_vowel):
            last_vowel = char
        elif char not in vowels and rightmost_consonant is None:
            rightmost_consonant = char

    # Check if the above logic was executed correctly (consisting of only vowels or consonants)
    if last_vowel is None or rightmost_consonant is None:
        return ""

    # Return the closest vowel to the rightmost consonant
    if last_vowel == rightmost_consonant:
        return word[-1]
    else:
        return ""