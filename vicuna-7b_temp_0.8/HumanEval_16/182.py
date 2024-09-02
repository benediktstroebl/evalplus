

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # initialize a dictionary to keep track of the number of occurences for each character
    char_count = {}
    
    # loop through each character in the string
    for c in string:
        # check if the character is in the dictionary, if not increment the count by 1
        if c in char_count:
            char_count[c] += 1
        else:
            # add the character to the dictionary if it's not already there
            if c.lower() not in char_count:
                char_count[c.lower()] = 1
                
    # return the number of distinct characters
    return len(char_count)