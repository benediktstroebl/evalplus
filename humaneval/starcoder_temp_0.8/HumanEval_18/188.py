

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    assert isinstance(string, str), 'Expected a string'
    assert isinstance(substring, str), 'Expected a string'
    count = 0
    if len(substring) == 0:
        return count
    for i in range(len(string)):
        if string[i:i + len(substring)] == substring:
            count += 1
    return count
