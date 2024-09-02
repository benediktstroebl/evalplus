

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # given_string = str(given_string)
    # new_string = ''
    # for ch in given_string:
    #     if ch.isupper():
    #         new_string += ch.lower()
    #     elif ch.islower():
    #         new_string += ch.upper()
    #     else:
    #         new_string += ch
    # return new_string
    return string.swapcase()

