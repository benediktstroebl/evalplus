

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
    if string == '':
        return 0
    if len(string) < len(substring):
        return 0
    if string == substring:
        return 1
    if len(substring) == 1:
        return sum(string.count(substring))

    count = 0
    for i in range(len(string)):
        if string[i] == substring[0]:
            j = 0
            while string[i+j] == substring[j]:
                j += 1
                if j == len(substring):
                    count += 1
                    break
    return count

