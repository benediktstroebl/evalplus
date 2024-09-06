

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if len(substring) == 0:
        return 0
    substring_len = len(substring)
    counter = 0
    i = 0
    while i + substring_len <= len(string):
        if string[i:i+substring_len] == substring:
            counter += 1
        i += 1
    return counter

