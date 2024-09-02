

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if substring not in string:
        return 0
    split = string.split(substring)
    count = 0
    for i in split:
        if i == '':
            count += 1
    return count
