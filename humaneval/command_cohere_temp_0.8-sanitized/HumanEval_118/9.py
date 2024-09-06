def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming the vowels occur between two consonants.
    Ignores starting and ending vowels.
    """
    # Ensure input is lowercase
    word = word.lower()
    # Split the word into segments
    segments = word.split('')
    # Initialize variables to track the last encountered vowel's location and value.
    last_location = 0
    last_vowel = ''
    # Iterate through each character in the word.
    for i, char in enumerate(segments):
        # If the character is a vowel, set the last vowel and location.
        if char in 'aeiou':
            last_vowel = char
            last_location = i
        # If the character is a consonant and vowel occur after it, return the vowel.
        elif char in 'bcdfghjklmnpqrstvwxyz' and last_vowel:
            return last_vowel
    # If no eligible vowels are found, return an empty string.
    return ''