

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Initialize the count of distinct characters
    count = 0
    # Iterate over the string using a for loop
    for char in string:
        # If the current character is not in the dictionary, increment the count
        if char.lower() not in dictionary:
            count += 1
    return count