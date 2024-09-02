

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    counter = 0
    for _ in range(len(string)):
        idx = string.find(substring)
        if idx == -1:
            break
        counter += 1
        string = string[idx + 1:]

    return counter

