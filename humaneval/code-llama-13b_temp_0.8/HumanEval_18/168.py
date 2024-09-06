

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
    counter = 0
    while len(substring) <= len(string):
        if string.startswith(substring):
            counter += 1
            string = string[len(substring):]
        else:
            return counter
    return counter

