def get_closest_vowel(word):
    """
    Find the closest vowel to the right of consonant sequences in a string.
    
    Args:
        word (str): Input string.
    
    Returns:
        str: Closest vowel char to the right of consonant sequences or an empty string.
    """
    vowels = 'AEIOUaeiou'  
    # Convert to lowercase to handle case insensitivity
    word = word.lower()
    # Split the word into individual chars and initialize the flag
    chars = list(word)
    found = False

    # Iterate through each char in the word
    for i in range(len(chars)):
        char = chars[i]
        # If current char is a vowel and not the last char, move to the next iteration
        if char in vowels and i < len(chars) - 1:
            continue
        # If current char is a consonant and the next char is a vowel, set the flag true
        elif char not in vowels and i < len(chars) - 1 and chars[i+1] in vowels:
            found = True
        # If a consonant sequence is found and the flag is false, return an empty string
        elif char not in vowels and not found and i < len(chars)-1:
            return ''
        # Set the flag true whenever a vowel is encountered in a consonant sequence
        found = False
    # Return the last char if the flag is true, otherwise an empty string
    return chars[-1] if found else ''