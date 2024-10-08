def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to ignore case
    string = string.lower()
    
    # Create a set of characters in the string
    distinct_chars = set(string)
    
    # Return the length of the set as the number of distinct characters
    return len(distinct_chars)
