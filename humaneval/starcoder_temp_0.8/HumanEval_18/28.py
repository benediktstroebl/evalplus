

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
    if string == '':
        return 0
    if string == substring:
        return 1
    for index in range(len(string)):
        if string[index] == substring[0]:
            if string[index:index+len(substring)] == substring:
                count += 1
    return count

