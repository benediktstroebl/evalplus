

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    result = 0
    while True:
        result += 1
        found = string.find(substring, 0)
        if found == -1:
            break
        string = string[found + 1:]
    return result
