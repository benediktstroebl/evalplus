

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    if not string or not substring:
        return 0

    num = 0
    i = 0
    while i != -1:
        i = string.find(substring, i)
        if i != -1:
            num += 1
            i += 1
    return num
