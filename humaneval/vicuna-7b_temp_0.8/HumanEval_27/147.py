

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # Create a set to store the characters that should be flipped
    characters_to_flip = frozenset(string.lower()) | frozenset(string.upper())
    
    # Convert the string to a list of characters
    char_list = string.chars()
    
    # Iterate through the characters and flip them if they are in the set of characters to flip
    for i, char in enumerate(char_list):
        if char in characters_to_flip:
            char_list[i] = chr(ord(char) ^ 0x1F)
    
    # Convert the list of characters back to a string
    return ''.join(char_list)
