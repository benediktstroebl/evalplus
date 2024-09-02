

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    # count how many times the substring can be found
    count = 0

    # check if the substring is empty
    if substring == '':
        return 0

    # check if the substring is smaller than the original string
    if len(substring) <= len(string):
        # loop through the string
        for i in range(len(string)):
            # check if the substring can be found in the original string
            if string[i: i + len(substring)] == substring:
                count += 1
    return count

