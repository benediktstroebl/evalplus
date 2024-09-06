

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    def count_characters(char: str, string: str):
        """ Given a character and a string, return the count of that character in the string
        >>> count_characters('x', 'xyz')
        1
        >>> count_characters('x', 'xyzxyz')
        2
        >>> count_characters('y', 'xyz')
        1
        """
        count = 0
        for ch in string:
            if ch.casefold() == char.casefold():
                count += 1
        return count

    char_count = 0
    for ch in string:
        char_count += count_characters(ch, string)
    return char_count

