

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """

    # approach 1: concatinate strings
    # result = '0'
    # for i in range(1, n + 1):
    #     result += ' ' + str(i)
    # return result

    # approach 2: create a list
    result = []
    for i in range(n + 1):
        result.append(str(i))
    return ' '.join(result)

