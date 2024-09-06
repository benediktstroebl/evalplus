def flip_case(string: str) -> str:
    """
    Flip lowercase characters to uppercase and uppercase characters to lowercase in a string.
    :param string: String to transform.
    :return: The transformed string.
    """
    # Use a list comprehension to split string into list of characters and then swap case for each character.
    return ''.join(char.swapcase() for char in string)