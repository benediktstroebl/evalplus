

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    # Instantiate a dictionary to hold unique values
    dict = {}

    # Lowercase the string
    string = string.lower()

    # Loop through the string and add values to the dictionary
    for char in string:
        dict[char] = None

    return len(dict.keys())

