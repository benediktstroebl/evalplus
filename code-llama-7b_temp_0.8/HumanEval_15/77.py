

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    # create a variable to store the string to return.
    str_seq = ''
    # if n is less than or equal to 0, set it to 0
    if n <= 0:
        n = 0
    # For every number in the range [0, n], append the string representation of the number to the variable str_seq.
    for i in range(n + 1):
        str_seq = str_seq + str(i) + ' '

    return str_seq

