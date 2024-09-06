

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

    if string == substring:
        return len(string)

    if string == '':
        return 0

    if len(string) < len(substring):
        return 0

    if string.count(substring) > 0:
        return string.count(substring)

    return len(substring) - (len(substring) - string.count(substring))
