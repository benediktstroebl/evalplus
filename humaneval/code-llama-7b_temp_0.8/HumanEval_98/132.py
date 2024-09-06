
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # set up a counter for the number of uppercase vowels in even-indexed positions
    # count up the number of vowels in even-indexed positions
    # return the number of vowels counted
    counter = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i].isupper():
            counter += 1
    return counter
