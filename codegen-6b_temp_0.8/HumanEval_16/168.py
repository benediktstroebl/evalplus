

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    string = string.lower()
    char_sum = 0
    for char in string:
        if char_sum < string.count(char):
            char_sum = string.count(char)
    print(char_sum)

