

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    if len(substring) > len(string):
        return 0
    if len(substring) == len(string):
        return 1
    if len(substring) == 0:
        return len(string)

    counter = 0
    for i in range(len(string)-len(substring)+1):
        if string[i] == substring[0]:
            count = 1
            for j in range(1, len(substring)):
                if string[i+j] == substring[j]:
                    count += 1
                else:
                    break
            if count == len(substring):
                counter += 1
    return counter

