

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if substring == '':
        return len(string) + 1
    if substring in string:
        return 1 + how_many_times(string[string.index(substring) + 1:], substring)
    return 0

