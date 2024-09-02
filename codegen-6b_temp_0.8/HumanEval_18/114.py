

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
    i_sub = 0
    i_str = 0
    while i_str < len(string):
        i_sub = string.find(substring, i_sub)
        if i_sub == -1:
            break
        else:
            i_str = i_sub + 1
            count += 1
    return count

