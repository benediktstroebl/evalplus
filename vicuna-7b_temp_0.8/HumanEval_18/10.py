

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if string == '' or substring == '':
        return 0
    elif string == substring:
        return 1
    else:
        start = 0
        count = 1
        for i in range(len(string)):
            if substring[i] != string[i]:
                start = i
                break
        for i in range(len(string) - len(substring)):
            if string[i:i+len(substring)] == substring:
                count += 1
        return count