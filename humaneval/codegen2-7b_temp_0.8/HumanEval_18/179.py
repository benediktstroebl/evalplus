

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
    if len(string) == 0:
        return count
    if len(substring) == 0:
        return count
    for i in range(len(string)):
        if string[i] == substring[0]:
            count += how_many_times(string[i + 1:], substring[1:])
    return
