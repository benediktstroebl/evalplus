

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    count: int = 0
    start: int = 0
    while True:
        start = string.find(substring, start)
        if start == -1:
            break
        count += 1
        start += 1
    return count
