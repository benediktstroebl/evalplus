

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    assert len(string) >= len(substring)
    return len([1 for i in range(0, len(string), 1) if string[i:i+len(substring)] == substring])


from functools import lru_cache
