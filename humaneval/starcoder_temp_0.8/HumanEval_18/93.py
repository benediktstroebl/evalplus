

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if string == '':
        return 0
    if string == substring:
        return 1
    if len(string) < len(substring):
        return 0
    if len(string) == len(substring):
        return 1
    return 1 + how_many_times(string[1:], substring) + how_many_times(string[1:], substring[1:])
