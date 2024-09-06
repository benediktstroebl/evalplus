

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    num = 0
    i = 0
    while i < len(string):
        if string[i] == substring[0]:
            j = 0
            while j < len(substring) and string[i] == substring[j]:
                i += 1
                j += 1
            if j == len(substring):
                num += 1
        i += 1
    return num

