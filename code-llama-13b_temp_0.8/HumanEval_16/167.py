

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    # Time Complexity : O(n)
    # Space Complexity : O(n)
    
    # hashset = set()
    # for char in string:
    #     hashset.add(char.lower())
    # return len(hashset)

    # Time Complexity : O(n)
    # Space Complexity : O(1)
    return len(set(string.lower()))

