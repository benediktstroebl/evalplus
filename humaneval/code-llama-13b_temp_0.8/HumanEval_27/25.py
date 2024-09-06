

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    string = list(string)

    for index in range(len(string)):
        if string[index].isalpha():
            string[index] = string[index].swapcase()

    return ''.join(string)

