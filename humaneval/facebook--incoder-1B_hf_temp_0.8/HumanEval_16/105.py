def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    chars = string.lower()
    occurrences = collections.Counter()
    for char in chars:
        occurrences[char] += 1
    return occurrences.most_common()[-1][0]

