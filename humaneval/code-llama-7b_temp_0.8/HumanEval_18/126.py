

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    found_counter = 0

    for index in range(len(string) - len(substring) + 1):
        if string[index:index+len(substring)] == substring:
            found_counter += 1

    return found_counter
