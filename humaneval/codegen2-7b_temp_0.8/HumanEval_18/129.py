

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    cnt = 0
    for i, x in enumerate(string):
        if x == substring[0]:
            cnt += 1
            if len(substring) == 1:
                return cnt
            if string[i + 1:] == substring[1:]:
                cnt -= 1
                if cnt < 0:
                    break
    return c
