

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    substr_count = 0
    substr_len = len(substring)
    for i in range(len(string) - substr_len + 1):
        if string[i:i + substr_len] == substring:
            substr_count += 1
    return substr_count

