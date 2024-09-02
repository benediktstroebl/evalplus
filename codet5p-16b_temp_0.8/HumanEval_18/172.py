

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

    total_occurances = 0
    prev_index = 0
    for index in range(len(string)):
        if string[index] == substring[0]:
            if string[prev_index:index] == substring[prev_index:index]:
                total_occurances += 1
                prev_index = index
    return total_occurances

