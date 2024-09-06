

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if not substring or not string:
        return 0

    n_substring = len(substring)
    n_string = len(string)
    if n_substring > n_string:
        return 0

    return string.count(substring, 0, n_string - n_substring + 1)

