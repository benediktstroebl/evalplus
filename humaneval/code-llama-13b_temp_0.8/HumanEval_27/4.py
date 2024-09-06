

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    out_string = ''
    for c in string:
        if c in uppercase:
            out_string += lowercase[uppercase.index(c)]
        else:
            out_string += uppercase[lowercase.index(c)]
    return out_string

