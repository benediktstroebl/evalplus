

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

    if len(string) == 0:
        return 0

    counter = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i] == substring[0]:
            flag = True
            for j in range(len(substring)):
                if string[i+j]!= substring[j]:
                    flag = False
                    break
            if flag:
                counter += 1
    return counter

