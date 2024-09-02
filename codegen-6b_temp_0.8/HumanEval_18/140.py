

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    # how many times substring can be found?
    if substring == '' or string == '':
        return 0
    # count the number of cases for each string in the beginning
    beginning_count = 0
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            beginning_count += 1
    return beginning_count
