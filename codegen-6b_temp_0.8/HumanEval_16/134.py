

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # If string is empty, return 0
    if string == '':
        return 0
    # If string is of length 1, return 1
    if len(string) == 1:
        return 1

    # Initialize a zero count
    count = 0

    # Iterate over the string
    for char in string:
        if char.lower() < char.upper():
            # If the current character is a lowercase, increase the count
            count += 1

    # Return the count
    return count
