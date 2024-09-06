

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
    for i in range(len(string)):
        if substring[i] == string[i]:
            count += 1
            start = i + 1
            while start < len(substring) and substring[start] == string[i + start - 1]:
                start += 1
            if start > len(substring):
                break
    return count
