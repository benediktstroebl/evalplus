

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
    start_pos = 0
    for i in range(len(string)):
        if substring[i] == string[i]:
            count += 1
            start_pos = i + 1
            while start_pos < len(string) and substring[start_pos] == string[start_pos]:
                start_pos += 1
        else:
            break
    return count