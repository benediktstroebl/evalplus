

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    string_counter = 0
    substring_counter = 0
    while substring_counter < len(string):
        if string[substring_counter] == substring[substring_counter]:
            substring_counter += 1
        else:
            string_counter += 1
            substring_counter = 0
        if substring_counter == len(substring) - 1:
            string_counter += 1
    return string_counter
