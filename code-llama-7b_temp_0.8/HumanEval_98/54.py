
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # return the number of vowels in even positions
    # initialize count to zero
    count = 0
    # for each letter in s
    for i in range(len(s)):
        # check if the letter is in the set of vowels
        if (s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U'):
            # check if the letter is in an even position
            if (i % 2 == 0):
                # increment count
                count = count + 1
    return count
