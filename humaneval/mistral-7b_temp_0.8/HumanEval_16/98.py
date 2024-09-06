

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    # TODO: Write your code here
    #   > Create a set that you'll use to store the characters.
    #   > Loop through the input string, and use the in operator to determine if each character is in the set.
    #   > If not, add the character to the set.
    #   > Return the length of the set.
    charset = set()
    for letter in string:
        if letter in charset:
            pass
        else:
            charset.add(letter)

    return len(charset)

