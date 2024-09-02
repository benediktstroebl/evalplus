

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    if substring == '':
        return 0

    # Initialize count to 0.
    count = 0

    # Find starting indices of all occurrences of substring in string.
    indices = [index for index in range(len(string)) if string.startswith(substring, index)]

    for index in indices:
        # Find all occurrences of substring in original string.
        count += string[index:].count(substring)
    return count

