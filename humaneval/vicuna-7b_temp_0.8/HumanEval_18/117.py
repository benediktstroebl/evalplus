

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
    start = 0
    while start < len(string) and string[start] == substring[0]:
        count += 1
        start += 1
        if start < len(substring):
            if string[start] == substring[1]:
                count += 1
                start += 1
    return count