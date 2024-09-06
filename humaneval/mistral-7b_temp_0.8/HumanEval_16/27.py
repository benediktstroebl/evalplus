

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # TODO
    # Hint: iterate over all characters in the string and check if any of them are already in a set.
    # If not, add it to the set. At the end of the iteration, return the size of the set.

    # to find the length of string
    # string_length = len(string)
    # print(string_length)

    # to make the string lowercase
    # string = string.lower()
    # print(string)

    # character_set = set()
    # for character in string:
    #     if character not in character_set:
    #         character_set.add(character)
    # print(character_set)

    # return len(character_set)

    # 2nd approach using set() function
    set_of_characters = set()

    for character in string:
        if character.lower() not in set_of_characters:
            set_of_characters.add(character.lower())

    # print(set_of_characters)

    return len(set_
