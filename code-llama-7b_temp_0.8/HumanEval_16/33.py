

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Work with the lowercase version of the string
    lowercase_string = string.lower()
    # Create a set with the characters of the string
    distinct_characters_set = set(lowercase_string)
    return len(distinct_characters_set)
