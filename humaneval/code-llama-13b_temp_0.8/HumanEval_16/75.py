

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    # Time Complexity: O(n), Space Complexity: O(n)
    characters_set = set()
    for character in string:
        characters_set.add(character.lower())
    return len(characters_set)

    # Time Complexity: O(nlogn), Space Complexity: O(1)
    # return len(sorted(string.lower()))

    # Time Complexity: O(n), Space Complexity: O(1)
    # characters = [False] * 26
    # for character in string:
    #     index = ord(character.lower()) - 97
    #     if not characters[index]:
    #         characters[index] = True
    # return sum(characters)

