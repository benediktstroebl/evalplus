

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    # Define function using slicing
    return string[::-1].swapcase()

    # Define function using the built-in str.swapcase()
    # return string[::-1].swapcase()
