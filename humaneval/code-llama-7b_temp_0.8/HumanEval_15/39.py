

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """

    # Your code here
    # i will be the index variable.
    # s will be the string variable.
    # result will be the return value.
    i = 0
    s = ''
    result = ''

    # looping the numbers from 0 to n
    while i <= n:
        s += str(i)
        i += 1

    # break the number string into list of characters and join them back with space as delimiter
    result = ' '.join(list(s))

    # return the string
    return result

