

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if len(string) == 0 or substring in string:
        return 0
    elif substring in string:
        count = 1
        start = 0
        for i in range(len(string)):
            if substring in string[i:]:
                count += 1
                start = i
        return count + how_many_times(string[start:], substring)
    else:
        return 0
