

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # new_string = ''
    # for letter in string:
    #     if letter.islower():
    #         new_string += letter.upper()
    #     if letter.isupper():
    #         new_string += letter.lower()
    # return new_string
    new_string = string.swapcase()
    return new_string
