

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    counter = 0
    for i in range(0, len(string)):
        if string[i] == substring[0]:
            j = i
            while j < len(string):
                if string[j] == substring[1]:
                    counter += 1
                    j += 1
                else:
                    break
    return
