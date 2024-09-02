

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    if len(string) == 0:
        return 0
    else:
        current_char = string[0]
        total_distinct = 0
        for char in string:
            if char.upper() == current_char.upper():
                pass
            else:
                total_distinct += 1
                current_char = char
        return total_distinct

