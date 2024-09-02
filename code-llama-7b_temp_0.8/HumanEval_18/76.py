

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    counter = 0
    idx = 0
    while idx != -1:
        idx = string.find(substring, idx)
        if idx != -1:
            idx += 1
            counter += 1
    return counter

