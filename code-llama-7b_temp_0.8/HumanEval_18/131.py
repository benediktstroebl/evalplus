

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    num_times = 0
    for index, letter in enumerate(string):
        try:
            if substring in string[index:index + len(substring)]:
                num_times += 1
        except IndexError:
            pass
    return num_times
