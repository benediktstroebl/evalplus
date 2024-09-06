

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    from string import ascii_lowercase, ascii_uppercase
    from collections import Counter

    return len(Counter(list(ascii_lowercase) + list(ascii_uppercase)).fromkeys(
        [char.lower() for char in string]))

