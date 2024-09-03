def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    distinct_count = Counter(string.lower())
    return sum(
        [
            1
            if char in distinct_count
            else 0
            for char in string
        ]
    )

