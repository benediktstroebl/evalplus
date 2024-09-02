

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
    if len(string) < len(substring):
        return 0
    if string == substring:
        return 1
    result = 0
    for i in range(len(string)):
        if string[i] == substring[0] and string[i:i + len(substring)] == substring:
            result += 1
    return result
