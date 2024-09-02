

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    sub_len = len(substring)
    string_len = len(string)

    if substring == '':
        return 0
    if string_len == 0:
        return 0

    count = 0
    i = 0

    while i < string_len:
        if string[i:i+sub_len] == substring:
            count += 1
            i += sub_len
        else:
            i += 1

    return count

