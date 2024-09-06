

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if string == '' and substring == '':
        return 0
    if substring in string:
        if len(substring) == 1:
            return 1
        if len(substring) >= len(string):
            return 0
        if len(substring) == 1 and len(string) == 2:
            return 2
        return how_many_times(string[1:], substring) + 1
    return 0

