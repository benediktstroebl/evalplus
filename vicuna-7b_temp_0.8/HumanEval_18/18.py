

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
    start_index = string.find(substring)
    end_index = string.rfind(substring)
    while start_index != -1 and end_index != -1:
        if start_index < end_index:
            count += 1
        start_index += len(substring)
        end_index += len(substring)
    return count