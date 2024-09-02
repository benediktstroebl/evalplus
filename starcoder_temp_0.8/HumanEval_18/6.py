

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    # The function should return 0 if either of the two strings is empty
    if string == '' or substring == '':
        return 0

    # The function should return the number of times the substring appears in the original string
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(substring):
            count += 1
    return count
