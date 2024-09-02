

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if substring == '' or substring is None:
        return 0

    count = 0
    while True:
        if substring in string:
            count += 1
            string = substring + string
        else:
            return count

