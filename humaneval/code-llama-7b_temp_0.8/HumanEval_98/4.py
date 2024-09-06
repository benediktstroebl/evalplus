
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # create counter to store number of uppercase vowels
    count = 0
    # loop over string
    for i in range(0, len(s), 2):
        # test if character is uppercase vowel
        if s[i].lower() in ['a','e','i','o','u']:
            # add 1 to counter if true
            count += 1
    return count
