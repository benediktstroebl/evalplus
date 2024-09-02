

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if len(string) == 0 or len(substring) == 0:
        return 0
    if len(string) == 1 and len(substring) == 1 and string == substring:
        return 1
    if len(string) < len(substring):
        return 0
    if len(string) == len(substring):
        if string == substring:
            return 1
        else:
            return 0
    count = 0
    start_index = 0
    while start_index < len(string) - len(substring) + 1:
        if string[start_index: start_index+len(substring)] == substring:
            count += 1
            start_index += len(substring) - 1
        start_index += 1
    return count

