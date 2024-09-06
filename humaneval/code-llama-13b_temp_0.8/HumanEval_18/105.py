

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if len(substring) == 0:
        return 0
    if len(string) < len(substring):
        return 0

    count = 0
    i = 0
    j = len(substring)

    while j <= len(string):
        if string[i:j] == substring:
            count += 1
            i += 1
            j += 1
        else:
            i += 1
            j = i + len(substring)

    return count

