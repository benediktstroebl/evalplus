

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    # If there is no string or substring return zero
    if not string or not substring:
        return 0

    overlaping_count = 0

    # Count overlaping occurrences
    for i in range(len(string)):
        if string[i : i + len(substring)] == substring:
            overlaping_count += 1

    return overlaping_count

