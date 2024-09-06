def flip_case(string: str) -> str:
    """
    Flip case of characters in a string. Shifts uppercase characters to lowercase and vice versa.
    
    Args:
    - string (str): Input string to modify
    
    Returns:
    - str: Modified string with flipped case
    
    Example:
    >>> flip_case('Hello World')
    'hELLO WORLD'
    """
    return string.swapcase()