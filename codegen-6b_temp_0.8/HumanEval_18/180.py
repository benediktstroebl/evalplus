

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if len(string) == 0:
        return 0
    if len(string) == 1:
        if substring in string:
            return 1
        else:
            return 0
    return how_many_times(string[1:], substring) + 1 if substring in string else how_many_times(string[1:], substring)

