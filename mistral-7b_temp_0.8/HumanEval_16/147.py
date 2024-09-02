

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Write your code here
    charset = set()
    for c in string:
        if c.lower() in charset:
            continue
        charset.add(c.lower())
    return len(charset)
