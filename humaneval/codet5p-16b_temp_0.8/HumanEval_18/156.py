

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
    if string.count(substring) == 0:
        return 0
    index = 0
    while True:
        if string.count(substring, index, index + len(substring)) > 0:
            count += 1
            index += len(substring)
        else:
            break
    return count
