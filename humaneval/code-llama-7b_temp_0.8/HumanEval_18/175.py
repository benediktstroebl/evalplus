

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if not string or not substring:
        return 0
    elif len(substring) > len(string):
        return 0
    elif substring == string:
        return 1

    occurrences = 0
    for i in range(len(string)):
        if string[i:].startswith(substring):
            occurrences += 1
    return occurrences

