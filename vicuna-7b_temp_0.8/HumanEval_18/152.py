

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
        if string[i] == substring[0]:
            count += 1
            i += 1
            while i < len(substring) and string[i] == substring[i]:
                i += 1
            if i >= len(substring):
                break
    return count