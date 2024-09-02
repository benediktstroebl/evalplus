

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
    if substring_len == 0:
        return 0
    if substring_len > len(string):
        return 0

    start = 0
    substring_num = 0

    while start < len(string):
        index = string.find(substring, start)
        if index == -1:
            break
        substring_num += 1
        start = index + 1

    return substring_num

