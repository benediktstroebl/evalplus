

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    flip_case_list = [x.swapcase() if x.islower() else x for x in string]
    return "".join(flip_case_list)

