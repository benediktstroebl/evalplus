

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if not string:
        return 0
    if not substring:
        return len(string)
    count = 0
    start = 0
    while start < len(string) and string[start] == substring[0]:
        start += 1
        count += 1
        if start + 1 < len(string) and string[start] == substring[1]:
            start += 2
        if start + 1 < len(string) and string[start] == substring[2]:
            start += 2
        if start + 1 < len(string) and string[start] == substring[3]:
            start += 2
    return count