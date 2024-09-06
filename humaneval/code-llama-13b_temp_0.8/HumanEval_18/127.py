

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
    length_string = len(string)
    length_substring = len(substring)
    if length_string < length_substring:
        return 0
    counter = 0
    for index in range(length_string - length_substring + 1):
        if string[index:index + length_substring] == substring:
            counter += 1
    return counter

