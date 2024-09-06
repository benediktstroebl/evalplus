def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring occurs in the original string, including overlapping occurrences.

    Examples:
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    string += substring
    return string.count(substring)