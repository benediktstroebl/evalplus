

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    occurrences = 0
    for index, value in enumerate(string):
        if value == substring[0]:
            if string[index: index + len(substring)] == substring:
                occurrences += 1
    return occurrences

