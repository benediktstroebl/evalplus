

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    pos = 0
    count = 0
    while pos < len(string):
        if string[pos:].startswith(substring):
            count += 1
            pos += len(substring)
        else:
            pos += 1
    return count

