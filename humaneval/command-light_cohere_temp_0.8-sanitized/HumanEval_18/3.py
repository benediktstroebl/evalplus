def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring in the original string.
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    >>> how_many_times('hello helloooo', 'hello')
    0
    >>> how_many_times('abcdeabcdeabcde', 'abc')
    5
    """
    n = string.count(substring)
    return n