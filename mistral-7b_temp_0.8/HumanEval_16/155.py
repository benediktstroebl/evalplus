

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # we'll use a dictionary to count the occurrences of each character
    # (including case sensitivity)
    char_counter = {}

    # go through the string once to count the occurrences of each character
    for letter in string:
        # if the character is not in our dictionary, add it with a count of 1
        if letter not in char_counter:
            char_counter[letter] = 1
        else:
            # otherwise, increment the count of this character
            char_counter[letter] += 1

    # now, return the total count of characters
    return len(char_counter)

