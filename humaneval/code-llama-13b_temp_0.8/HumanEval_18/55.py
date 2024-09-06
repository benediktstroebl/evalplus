

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    if not string:
        return 0
    if len(string) < len(substring):
        return 0
    elif string == substring:
        return 1
    elif len(substring) == 1:
        return string.count(substring)
    else:
        return how_many_times(substring, string[1:]) + how_many_times(string[1:], substring)

