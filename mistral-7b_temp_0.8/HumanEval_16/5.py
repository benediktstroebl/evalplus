

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Your code here
    # O(n)
    temp_string = string.lower()
    count = 0
    for i in range(len(temp_string)):
        if temp_string[i] not in string:
            count += 1
    return count

