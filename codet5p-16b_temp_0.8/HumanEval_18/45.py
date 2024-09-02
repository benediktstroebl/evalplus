

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    counter: int = 0
    i: int = 0
    n: int = len(string)
    m: int = len(substring)
    while i < n:
        if string[i:i + m] == substring:
            counter += 1
            i += m
        else:
            i += 1
    return counter
