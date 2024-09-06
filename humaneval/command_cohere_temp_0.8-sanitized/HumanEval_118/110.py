def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming vowels at the start and end do not count.
    Empty string is returned if no such vowel exists.
    """
    # Ensure the word has only alphabetic characters
    if not all(isinstance(c, str) and c.isalpha() for c in word):
        raise ValueError("Input contains non-alphabetic characters")
        
    # Split the word into individual characters and initialize the right-most vowel index
    chars, vowel_idx = zip(*word.lower().rstrip('aeiou').split(''))
    # Reverse the list of characters to orient towards the right side
    chars = list(reversed(chars))
    # Initialize an empty string to hold the closest vowel
    closest_vowel = ''
    # Initialize a flag to determine if any vowels exist in the word
    has_vowels = False
    
    # Iterate through the characters from right to left, looking for vowels afterconsonants
    for i, char in enumerate(chars):
        if char in 'aeiou' and (i == 0 or chars[i-1] in 'bcdfghjklmnpqrstvwxyz'):
            # If a vowel is found between two consonants, set the closest vowel and return
            closest_vowel = char
            has_vowels = True
            break
    
    # If no vowel was found between consonants, return an empty string
    return closest_vowel if has_vowels else ''