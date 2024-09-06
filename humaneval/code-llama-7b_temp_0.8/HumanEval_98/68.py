
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    #initialize counter at 0
    num_upper = 0

    #iterate through string, start at 1
    for i in range(1, len(s), 2):

        #if s[i] is uppercase, increase counter by 1
        if s[i].isupper():
            num_upper += 1

    return num_upper

