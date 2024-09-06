

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(
        char*2 if index%2 == 1 else char.swapcase()
        for index, char in enumerate(string)
    )

