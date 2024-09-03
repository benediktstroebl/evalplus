def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Python does not have an inbuilt string function, so use an intermediate variable
    stringcase = ""
    for i in string:
        stringcase += i.upper()
        stringcase += i.lower()
        stringcase += i.capitalize()
    return len(stringcase)

