

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # case_state = string.islower()  # Boolean indicating whether string is lowercase or not.
    # new_case = lambda char: char.upper() if case_state else char.lower()
    # new_string = ''.join(map(new_case, string))
    # return new_string
    return ''.join([char.upper() if char.islower() else char.lower() for char in string])


