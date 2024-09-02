

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # if you are allowed to use other libraries like collections:
    # return len(set(string))

    # implement it yourself
    # set takes care of case insensitive
    count = 0
    set_of_string = set(string)
    for i in set_of_string:
        count += 1
    return count

