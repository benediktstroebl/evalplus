

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    substring_len = len(substring)
    first_substring_index = string.find(substring)
    count = 0

    while first_substring_index != -1:
        count += 1
        first_substring_index = string.find(substring, first_substring_index + substring_len)

    return count
