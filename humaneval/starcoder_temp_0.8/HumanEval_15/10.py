

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    # The following is a list comprehension.  It creates a list of numbers from 0 to n
    # inclusive.  This list is then converted to a string by calling join() on the list with
    # the separator string " ".  The final expression calls join() again but this time using
    # the separator string ", " (comma + space).
    #
    # In summary, the list comprehension says:
    #    "Return a list of n numbers from 0 to n inclusive. Convert the list to a string by
    #    using the space character as the separator and the comma character as the terminator.
    #    Finally, return the string value by using a colon as the separator."
    #
    return''.join([str(i) for i in range(n+1)]) + ','+ ','.join([str(i) for i in range(n+1)])
