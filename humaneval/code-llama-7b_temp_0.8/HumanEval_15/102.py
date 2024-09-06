

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """

    # the result string
    string = ""

    # for i in range(n)
    for i in range(n):
        # add i to the result string
        string += str(i)

        # add a space if i is less than n
        if i < n - 1:
            string += " "

    # return the result string
    return string

