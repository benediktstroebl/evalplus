

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
    string_index = 0
    while string_index < len(string):
        substring_index = string_index
        while substring_index < len(string):
            if string[substring_index: substring_index + len(substring)] == substring:
                count += 1
                break
            substring_index += 1
        string_index += 1
    return count
