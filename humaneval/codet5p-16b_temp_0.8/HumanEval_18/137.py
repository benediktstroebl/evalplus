

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    total = 0
    index_substr = 0
    for i in range(len(string)):
        if string[i] == substring[index_substr]:
            index_substr += 1
            if index_substr == len(substring):
                total += 1
                index_substr = 0
        else:
            index_substr = 0

    return total

