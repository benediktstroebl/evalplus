

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    assert isinstance(string, str)
    assert isinstance(substring, str)

    index = string.find(substring)

    if index == -1:
        return 0
    else:
        return 1 + how_many_times(string[index + len(substring):], substring)

