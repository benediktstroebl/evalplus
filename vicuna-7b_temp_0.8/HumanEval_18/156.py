

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
    start = 0
    end = 0
    for i in range(len(string)):
        if string[i:i+1] == substring:
            count = count + 1
            start = i + 1
            end = len(string)
        elif string[i] == substring[end-1]:
            count = count + 1
            start = i + 1
        elif string[i] == substring[0]:
            count = count + 1
            start = i + 1
            end = i + 1
    return count