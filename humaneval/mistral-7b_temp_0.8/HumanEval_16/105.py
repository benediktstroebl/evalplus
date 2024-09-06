

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # TODO: Implement this function
    # First convert the string to lowercase so we can just worry about lowercase characters
    lowercase_string = string.lower()
    # Initialize a variable to count the distinct characters
    distinct_chars = 0
    # Iterate over every character in the string
    for char in lowercase_string:
        # If the character is not already in the set, append it to the set
        if char not in distinct_chars:
            distinct_chars.add(char)
    return len(distinct_chars)
