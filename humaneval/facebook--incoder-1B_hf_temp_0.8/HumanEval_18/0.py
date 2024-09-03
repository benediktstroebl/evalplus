def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if len(string) <= 1 or len(substring) <= 1:
        return 0
    
    count = [0] * len(string)
    count[0] = string.count(substring[0])
    for i in range(1, len(string)):
        count[i] = string.count(substring, i)
    
    return sum(count[:len(string) - 1])

