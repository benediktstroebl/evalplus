

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    count = 0
    start = string.find(substring)
    end = string.rfind(substring)
    for start in range(min(start, end), len(string)):
        end = string.rfind(substring, start)
        if end == -1 or end > end:
            count += 1
    return count