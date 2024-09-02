

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
    index = 0
    for i in range(len(string)):
        if string[i] == substring[0]:
            count += 1
            index = i
            for j in range(len(substring)):
                if substring[j] != string[index+j]:
                    count -= 1
                    index = i
                    break
    return count