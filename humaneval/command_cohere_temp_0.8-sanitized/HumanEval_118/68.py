def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming consonants sandwiching it.
    Ignores starting and ending vowels.
    """
    # Ensure input is lowercase for consistency
    word = word.lower()
    word = word.strip('aeiou')

    # Ensuring the word ends with a consonant to avoid unnecessary next checks
    if word.endswith('a') or word.endswith('e') or word.endswith('i') or word.endswith('o') or word.endswith('u'):
        return ''

    # Special case for single character words (assuming consonants)
    if len(word) == 1:
        return ''

    # Iterating through potential vowels to find the first one that matches our criteria
    for vowel in 'aeiou':
        if vowel in word:
            # Checking if a consonant follows the found vowel
            if word.split(vowel)[1].isalpha():
                return vowel

    # If no matches are found, return an empty string
    return ''