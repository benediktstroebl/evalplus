def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    if len(string) <= 1:
        return 1

    # A dictionary can be used to map each character to its count
    count_map = {}

    for char in string:
        if char in count_map:
            count_map[char] += 1
        else:
            count_map[char] = 1

    # Return the number of distinct characters
    return len(count_map)

