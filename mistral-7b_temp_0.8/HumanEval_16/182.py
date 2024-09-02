

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    distinct = 0
    lower_string = string.lower()
    for char in lower_string:
        if lower_string.count(char) == lower_string.count(char.upper()):
            distinct += 1
        elif lower_string.count(char) > lower_string.count(char.upper()):
            distinct += 1
    return distinct

