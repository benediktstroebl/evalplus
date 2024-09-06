

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    # create dictionary, let keys be characters and values be count of the character
    char_count = dict()

    for i in string:
        if i not in char_count:
            char_count[i] = 1
        else:
            char_count[i] += 1

    # find out the number of distinct characters
    distinct_char = 0

    for i in char_count:
        distinct_char += 1

    return distinct_char

