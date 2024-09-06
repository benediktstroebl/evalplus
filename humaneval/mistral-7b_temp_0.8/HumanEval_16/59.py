

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    from string import ascii_lowercase
    from string import ascii_uppercase
    char_set = set(ascii_lowercase) | set(ascii_uppercase)
    char_set = frozenset(char_set)

    def is_distinct(char: str) -> bool:
        return char in char_set

    def count_distinct_chars(string: str) -> int:
        chars = set(string)
        return len(list(filter(is_distinct, chars)))

    return count_distinct_chars(string)
