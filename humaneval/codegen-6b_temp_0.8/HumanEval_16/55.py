

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # an alternative approach using Counter
    # from collections import Counter
    # return sum(1 for char, count in Counter(string.lower()).items() if count == 1) 

    # alternatively, using python dict.
    distinct_chars = {}
    for char in string:
        if char.lower() in distinct_chars:
            distinct_chars[char.lower()] += 1
        else:
            distinct_chars[char.lower()] = 1
    
    return sum(distinct_chars.values())
