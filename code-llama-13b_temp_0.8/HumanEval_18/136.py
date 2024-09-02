

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    n = len(string)
    if n == 0 or substring == '':
        return 0
    # counter
    counter = 0
    # starting index of the substring
    start = 0
    # run loop till start becomes n
    while start < n:
        # search for the substring from start to n
        s = string.find(substring, start, n)
        # if the substring is found
        if s != -1:
            # increase the counter
            counter = counter + 1
            # increase the start index
            start = s + 1
        else:
            break
    return counter

