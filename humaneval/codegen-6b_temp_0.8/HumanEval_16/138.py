

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    if len(string) == 1:
        return 1

    # If the input string is more than 1 character,
    # we can't use array but we can use hashmap to divide the string into chunks of
    # equal size and see how many distinct characters each chunk has
    char_hashtable = {}
    current_index = 0

    while current_index < len(string):
        # check if we have seen this character before
        if string[current_index].lower() not in char_hashtable:
            char_hashtable[string[current_index].lower()] = 1
        else:
            char_hashtable[string[current_index].lower()] += 1

        current_index += 1

    sorted_char_hashtable = sorted(char_hashtable.items(), key=operator.itemgetter(1), reverse=True)
    return len(sorted_char_hashtable)
