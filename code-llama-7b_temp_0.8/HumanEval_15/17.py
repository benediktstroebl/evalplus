

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """

    # This is a pretty inefficient solution, as we will be
    # creating a string for each element of the output.
    # We return a single string at the end by concatenating
    # all of the strings we have created.
    output = ''
    for i in range(n + 1):
        output += str(i) + ' '

    return output[:-1]
    # Alternatively, we can use the join function to create
    # our output string:
    # return ' '.join(str(i) for i in range(n+1))

