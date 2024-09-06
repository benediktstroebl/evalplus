

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    i = start = 0
    while i < len(string):
        start = string.find(substring, start)
        if start == -1:
            return i
        start += 1
        i += 1
    return i

