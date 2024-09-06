

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    chars_dict = {}
    for ch in string:
        if ch.lower() not in chars_dict.keys():
            chars_dict[ch.lower()] = 1
        else:
            chars_dict[ch.lower()] += 1
    print(chars_dict)
    return len(chars_dict.keys())

