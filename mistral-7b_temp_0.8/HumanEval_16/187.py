

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    # Convert the string to lower case
    string = string.lower()

    # Count distinct characters in the string
    distinct_characters = len(set(string))

    return distinct_characters

