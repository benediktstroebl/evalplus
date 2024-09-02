

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """

    def make_list(n):
        return list(range(n + 1))

    def make_string(list):
        return ' '.join(map(str, list))

    return make_string(make_list(n))


