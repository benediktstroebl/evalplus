

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    distinct_chars = {}
    current_char = ""
    for char in string:
        if char.lower() not in distinct_chars:
            distinct_chars[char.lower()] = 1
            if current_char != "":
                distinct_chars[current_char] += 1
            current_char = char
    return len(distinct_chars)
