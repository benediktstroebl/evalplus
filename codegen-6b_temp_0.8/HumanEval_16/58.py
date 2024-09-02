

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    distinct_characters = set()

    for letter in string:
        if letter.isalpha():
            if letter.lower() not in distinct_characters:
                distinct_characters.add(letter.lower())
        else:
            distinct_characters.add(letter)
    return len(distinct_characters)

