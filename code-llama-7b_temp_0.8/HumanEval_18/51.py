

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
    count = 0
    for i in range(len(string)):
        if string[i] == substring[0]:
            flag = True
            for j in range(len(substring)):
                if string[i + j] != substring[j]:
                    flag = False
                    break
            if flag:
                count += 1
    return count

