

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Solution 1
    # O(n log n) time - sorting is O(n log n)
    # O(n) space - extra list to store sorted copy of input
    # return len(sorted(list(set(string))))

    # Solution 2
    # O(n) time - we only have a single iteration on string
    # O(1) space - we don't use any additional memory, only the input itself is used
    distinct_characters = set()
    for character in string:
        distinct_characters.add(character.lower())

    return len(distinct_characters)

