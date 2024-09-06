def flip_case(string: str) -> str:
    """
    Flip lowercase characters to uppercase and uppercase characters to lowercase in a string.
    """
    # Use a list comprehension to iterate through each character in the string
    return ''.join(char.swapcase() for char in string)