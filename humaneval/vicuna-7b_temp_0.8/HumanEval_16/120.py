

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Use a dictionary to store the count of each character, with the count initialized to 0
    char_count = {}

    # Iterate over the string using a for loop
    for char in string:
        # Get the Unicode code point of each character
        code_point = unichr(ord(char))

        # If the character is already in the dictionary, increment its count
        if code_point in char_count:
            char_count[code_point] += 1
        else:
            # If the character is not in the dictionary, add it with a count of 1
            char_count[code_point] = 1

    # Return the total count of distinct characters in the string
    return sum(char_count.values())