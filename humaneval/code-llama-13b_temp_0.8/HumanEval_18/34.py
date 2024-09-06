

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    # Base Case
    if len(string) == 0:
        return 0
    # Recursive Case
    elif substring == string[0:len(substring)]:
        return 1 + how_many_times(string[1:], substring)
    # Base Case
    else:
        return how_many_times(string[1:], substring)
