

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # if there's no character in the string, we're done
    if not string:
        return 0

    # iterate through every character of the string
    for char in string:
        # decrease the count of that character
        string = string.replace(char.lower(), '')
        string = string.replace(char.upper(), '')

    return len(string)




