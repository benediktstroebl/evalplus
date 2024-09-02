

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    overlapping = 0
    for i in range(0, len(string) - len(substring) + 1):
        if string[i] == substring[0]:
            overlapping += 1
            if len(substring) == 1:
                break
            if string[i + len(substring) - 1] == substring[len(substring) - 1]:
                overlapping -= 1
        if overlapping == len(substring):
            break
    return overlapping

