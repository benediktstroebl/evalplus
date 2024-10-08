

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    # Your code here
    if not substring:
        return 0

    count = 0
    idx = 0
    while True:
        idx = string.find(substring, idx)
        if idx != -1:
            count += 1
            idx += 1
        else:
            return count

