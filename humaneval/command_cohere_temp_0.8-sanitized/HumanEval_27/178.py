def flip_case(string: str) -> str:
    """
    Flip the case of alphabetic characters in a string, while leaving non-alphabetic characters unchanged.
    
    :param string: the input string
    :return: the processed string
    """
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)