

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    i, count = 0, 0
    while i < len(string):
        i = string.find(substring, i) + 1
        if i > 0:
            count += 1
    return count
