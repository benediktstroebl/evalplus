
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # set up counter
    counter = 0
    
    # check each even index
    for i in range(0, len(s), 2):
        # check if uppercase
        if s[i].isupper():
            # increment counter
            counter += 1
    # return counter
    return counter
