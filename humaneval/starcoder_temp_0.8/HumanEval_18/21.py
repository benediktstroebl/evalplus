

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
    i = 0
    while i < len(string):
        j = 0
        if string[i] == substring[j]:
            while i < len(string) and j < len(substring):
                if string[i] == substring[j]:
                    j += 1
                    i += 1
                else:
                    break
            if j == len(substring):
                count += 1
        else:
            i += 1
    return count
