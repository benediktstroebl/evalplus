def flip_case(string: str) -> str:
    """
    Flip uppercase characters to lowercase and lowercase characters to uppercase.
    :param string: String to transform.
    :return: The transformed string.
    """
    # Use a list comprehension to split string into list of characters and then swap cases
    return ''.join(char.swapcase() if char.islower() else char.upper() for char in string)