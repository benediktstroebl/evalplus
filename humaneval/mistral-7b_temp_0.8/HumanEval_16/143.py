

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # We need to use a set in order to not have duplicate values inside it
    # By using set() we also lower the case of the character which is very convenient
    # The trick is to iterate over each character inside the set
    # We know we have all characters, regardless of case, so we just have to check if
    # the value inside the set exists and if it does, we increment it by 1
    return len(set(string))

