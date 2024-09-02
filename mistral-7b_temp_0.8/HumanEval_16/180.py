

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    count_characters = 0

    # loop through the string
    for letter in string:
        # if the letter is a-zA-Z, increment the count
        if letter.isalpha():
            count_characters += 1

    return count_characters

