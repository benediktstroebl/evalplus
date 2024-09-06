

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    seen_string = set()

    for char in string:
        if char.isalpha():
            if char.lower() in seen_string:
                seen_string.remove(char.lower())
            else:
                seen_string.add(char.lower())

    return len(seen_string)

