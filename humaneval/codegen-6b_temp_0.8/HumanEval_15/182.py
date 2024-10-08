

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    string_list: list[str] = []
    for i in range(0, n + 1):
        string_list.append(str(i))
    return " ".join(string_list)
