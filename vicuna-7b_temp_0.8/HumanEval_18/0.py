

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
    for i in range(len(substring)):
        end_index = string.find(substring, start_index + i)
        if end_index == -1 or end_index == len(string) or (end_index == len(string) - 1 and string[end_index] != substring[i]):
            count += 1
    return count