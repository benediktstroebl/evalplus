def flip_case(string: str) -> str:
    """
    Flip case of characters in a string. Shifts uppercase characters to lowercase and vice versa.
    """
    return ''.join(char.swapcase() for char in string)