

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    if not string or not substring:
        return 0

    if substring == string:
        return 1

    count = 0
    while True:
        index = string.find(substring)
        if index == -1:
            return count
        count += 1
        string = string[index + 1:]

