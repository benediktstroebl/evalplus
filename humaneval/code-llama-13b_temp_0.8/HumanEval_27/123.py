

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # res = ''
    # for ch in string:
    #     if ch.islower():
    #         res += ch.upper()
    #     else:
    #         res += ch.lower()
    # return res
    return string.swapcase()

