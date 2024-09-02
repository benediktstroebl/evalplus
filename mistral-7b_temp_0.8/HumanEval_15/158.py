

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    # TODO: Implement me!
    # Replace this line with your code
    s = ""
    if n == 0:
        s = "0"
    elif n == 1:
        s = "0 1"
    else:
        for i in range(n):
            if i == 0:
                s = "0 "
            else:
                s = s + str(i) + " "

    return s

