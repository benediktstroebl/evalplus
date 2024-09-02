

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # Create a set of characters in the string
    char_set = string.lower()
    
    # Create a set of unique characters in the string
    unique_char_set = set(char_set)
    
    # Create a dictionary mapping lowercase characters to their uppercase equivalent
    mapping = {char: char.upper() for char in char_set}
    
    # Create a dictionary mapping uppercase characters to their lowercase equivalent
    mapping_inv = {char.upper(): char for char in char_set}
    
    # Flip the characters in the string
    flipped_string = ''
    for char in char_set:
        # If the character is in the set of unique characters, add it to the flipped string
        if char in unique_char_set:
            flipped_string += mapping[char]
        # If the character is in the set of unique characters, add it to the flipped string
        else:
            flipped_string += mapping_inv[char]
    
    return flipped_string
