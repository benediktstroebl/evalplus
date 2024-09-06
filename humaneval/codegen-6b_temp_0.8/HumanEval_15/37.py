

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    
    def inner(i: int) -> str:
        if i == 0:
            return "0"
        return inner(i - 1) + " " + str(i)
    
    return inner(n)
