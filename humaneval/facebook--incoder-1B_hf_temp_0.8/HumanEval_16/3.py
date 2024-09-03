def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Initialize count and set it to zero
    count = 0
    for i in range(len(string)):
        char = string[i]
        # Count the number of distinct characters
        if char in unique_characters:
            unique_characters.remove(char)
        else:
            count += 1

    return count

"""
Solution 2:
Given the string 'abcd', find the unique characters present in the string 'abcde'
"""

