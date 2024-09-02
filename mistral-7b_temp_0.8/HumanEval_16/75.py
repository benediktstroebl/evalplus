

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # 1. Transform string to lowercase
    lower_string = string.lower()

    # 2. Loop through each character in the string
    distinct_characters = set()
    for character in lower_string:
        distinct_characters.add(character)

    # 3. Count how many distinct characters
    return len(distinct_characters)
