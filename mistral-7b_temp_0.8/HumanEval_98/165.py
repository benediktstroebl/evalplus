
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    """
    This function takes a string as input and returns the number of uppercase vowels in even indices.
    It first initializes the count variable to 0.
    Then it loops through the string, checking each character to see if it is a vowel and whether it is in an even index.
    If both conditions are true, the count is incremented.
    Finally, the count is returned.
    """

    count = 0
    for i, char in enumerate(s):
        if char.isupper() and i % 2 == 0:
            count += 1
    return count
