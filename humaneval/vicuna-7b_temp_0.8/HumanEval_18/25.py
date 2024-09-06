

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if not string or not substring:
        return 0
    else:
        start_index = string.find(substring)
        end_index = string.rfind(substring) + 1
        count = 0
        for i in range(len(string)):
            if start_index <= i <= end_index and string[i:i+len(substring)] == substring:
                count += 1
        return count