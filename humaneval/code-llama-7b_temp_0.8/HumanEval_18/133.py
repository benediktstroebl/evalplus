

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if len(substring) == 0:
        return 0
    count = 0
    for i in range(len(string)):
        if string[i] == substring[0]:
            k = 0
            for j in range(i, len(string)):
                if substring[k] == string[j]:
                    k += 1
                    if k == len(substring):
                        count += 1
                        break
                else:
                    break
    return count

