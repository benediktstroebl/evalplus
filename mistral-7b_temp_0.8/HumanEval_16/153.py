

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # YOUR CODE HERE
    #return len(string)
    counter = 0
    for char in string:
        if char not in string:
            counter += 1
    return counter

