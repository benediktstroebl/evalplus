

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    string_index = 0
    substring_index = 0
    count = 0
    while string_index < len(string) and substring_index < len(substring):
        if string[string_index] == substring[substring_index]:
            string_index += 1
            substring_index += 1
        else:
            substring_index = 0
        count += 1
    return count

