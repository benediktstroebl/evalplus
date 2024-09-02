

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # hint: use a hash map to store counts of each character
    # hint: set() -> hash table from dict(), string -> list() -> join() -> generate a string
    distinct_characters = set()
    for character in string:
        distinct_characters.add(character)
    string = ''.join(distinct_characters)
    return len(string)

