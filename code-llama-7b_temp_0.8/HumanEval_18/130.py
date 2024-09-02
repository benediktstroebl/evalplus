

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if substring == '':
        return 0

    result = 0
    for i in range(len(string)):
        j = i
        while j < len(string) and substring[0] == string[j]:
            j += 1
            if j - i >= len(substring):
                result += 1
            if j == len(string):
                break
    return result
