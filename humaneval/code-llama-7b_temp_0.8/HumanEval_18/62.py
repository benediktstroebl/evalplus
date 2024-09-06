

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
    substring_length = len(substring)
    string_length = len(string)
    substring_idx = 0
    string_idx = 0

    while substring_idx < substring_length and string_idx < string_length:
        if substring[substring_idx] == string[string_idx]:
            substring_idx += 1
            string_idx += 1
        else:
            substring_idx = 0
            string_idx += 1
        if substring_idx == substring_length:
            count += 1
            substring_idx = 0

    return count

