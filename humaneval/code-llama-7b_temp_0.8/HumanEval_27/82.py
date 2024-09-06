

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # list_of_letters = list(string)
    # new_string = ''
    # for letter in list_of_letters:
    #     if letter.isupper():
    #         new_string += letter.lower()
    #     else:
    #         new_string += letter.upper()
    # return new_string
    return string.swapcase()
