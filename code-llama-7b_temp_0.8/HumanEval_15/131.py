

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    str_out = ""
    for i in range(n+1):
        str_out += str(i)
        if i != n:
            str_out += " "

    return str_out

