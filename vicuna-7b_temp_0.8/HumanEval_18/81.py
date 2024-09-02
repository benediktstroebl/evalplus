

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    count = 0
    index = 0
    start_index = 0
    for i in range(len(string)):
        if string[i:index] == substring:
            start_index = i
            count += 1
            if start_index == len(string) or string[start_index:start_index + len(substring)] == substring:
                count += 1
    return count