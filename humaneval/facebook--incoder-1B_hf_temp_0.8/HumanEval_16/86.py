def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    string = string.lower()
    return sum(
        (
            ord(c)
            for c in string
            if c in string.ascii_letters and c not in string.digits
        )
    )

