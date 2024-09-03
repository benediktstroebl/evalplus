def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    distinct_characters = 0
    distinct_char_count = 0

    for char in string:
        if char.isalpha():
            distinct_char_count = distinct_char_count + 1
        elif char.islower():
            distinct_characters = distinct_characters + 1

    return distinct_characters - distinct_char_count

