

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    # create an empty list.
    list = []
    # For loop from i = 0 to n-1.
    for i in range(n+1):
        # Append the list with the string of i.
        list.append(str(i))
    # Join the list with a space.
    final_string = ' '.join(list)
    return final_string
