

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
    for i in range(len(string)):
        if start_index + 1 <= i and string[i:i+len(substring)] == substring:
            count += 1
            start_index = i + len(substring)
    return count
