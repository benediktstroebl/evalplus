

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # Turn the string into a list of characters
    char_list = string.lower().split()
    # Loop through the list of characters and flip the case
    for i in range(len(char_list)):
        # If the current character is lowercase, make it uppercase
        if char_list[i].islower():
            char_list[i] = char_list[i].upper()
        # If the current character is uppercase, make it lowercase
        elif char_list[i].isupper():
            char_list[i] = char_list[i].lower()
    # Return the flipped string as a single string
    return ''.join(char_list)
