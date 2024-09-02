

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
    start = string.find(substring)
    end = string.rfind(substring) + 1
    while start != -1 and end != len(string):
        count += 1
        start, end = end, string.find(substring, end + 1)
    return count
