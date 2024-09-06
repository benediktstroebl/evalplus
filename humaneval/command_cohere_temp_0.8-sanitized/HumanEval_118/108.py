def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming the vowels occur between two consonants.
    Ignores starting and ending vowels.
    """
    # Ensure input is lowercase
    word = word.lower()
    # Split the word into segments
    segments = word.split('')
    # Initialize variables to track states
    right_consonant = False
    right_vowel = False
    # Iterate through each character in the word
    for char in segments:
        # If the character is a consonant and not at the beginning of a word
        if char in 'bcdfghjklmnpqrstvwxyz' and not right_consonant:
            # Toggle flag to indicate a consonant is found
            right_consonant = True
        # If the character is a vowel and not at the end of a word
        if char in 'aeiou' and not right_vowel:
            # Toggle flag to indicate a vowel is found
            right_vowel = True
        # If a consonant is followed by a vowel
        if right_consonant and right_vowel:
            # Return the most recent vowel (the one we just encountered)
            return char
    # If no vowel is found between two consonants
    return ""