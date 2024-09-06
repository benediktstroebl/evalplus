

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    count = 0
    string_start = 0

    while string_start < len(string):
        string_end = string_start + len(substring)

        if string_end > len(string):
            break

        if string[string_start:string_end] == substring:
            count += 1

        string_start += 1

    return count

