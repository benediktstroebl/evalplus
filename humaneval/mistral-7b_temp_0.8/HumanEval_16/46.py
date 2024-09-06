

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # initialize an empty dictionary
    distinct_chars_dict = {}
    # iterate over each character in the string
    for char in string:
        # check if the character already exists in the dictionary
        if char not in distinct_chars_dict:
            # if not, add it to the dictionary with a count of 1
            distinct_chars_dict[char] = 1
        # increment the count of the character if it already exists in the dictionary
        else:
            distinct_chars_dict[char] += 1
    return len(distinct_chars_dict)
