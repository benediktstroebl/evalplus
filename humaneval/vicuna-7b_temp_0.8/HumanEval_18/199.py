

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
    start = 0
    end = 0
    for i in range(len(string)):
        if string[i] == substring[start]:
            end = i
            start += 1
            if end == len(substring):
                count += 1
        else:
            break
    return count
