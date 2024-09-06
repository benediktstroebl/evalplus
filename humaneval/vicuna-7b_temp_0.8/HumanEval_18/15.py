

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
    index = 0
    start = 0
    while index < len(string) and start < len(substring):
        if string[index:start] == substring:
            start += len(substring)
        elif string[index:start] != substring and string[start:index] == substring:
            count += 1
            start = index + len(substring)
        index += 1
    return count