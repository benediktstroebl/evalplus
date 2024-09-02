

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if substring in string:
        count = 0
        i = 0
        for j in range(len(string)):
            if substring[i] != string[j]:
                count = 0
                break
            count += 1
            i += 1
        return count + (0 if substring[i] == string[j] else 1)
    return 0