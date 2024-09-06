

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if not substring:
        return 0
    substring_length = len(substring)
    count = 0
    start = 0
    while start < len(string):
        if string[start: start + substring_length] == substring:
            count += 1
            start += substring_length
        else:
            start += 1
    return count

