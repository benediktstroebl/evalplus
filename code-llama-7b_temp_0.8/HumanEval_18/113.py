

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    start = 0
    result = 0
    while start < len(string):
        start = string.find(substring, start)
        if start == -1:
            return result
        result += 1
        start += len(substring)
    return result

