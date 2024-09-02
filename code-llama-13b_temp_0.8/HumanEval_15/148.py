

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    x = 0
    y = 0
    #i = str(x)
    string = str(x)
    while x != n:
        x += 1
        string += " " + str(x)
    
    return string

