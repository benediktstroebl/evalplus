

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
    end = string.find(substring, start)
    while end != -1:
        count += 1
        start = end + len(substring)
        end = string.find(substring, start)
    return count