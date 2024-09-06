
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Your Code Here
    s_len = len(s)
    counter = 0
    for i in range(int(s_len/2)):
        if s[i].isupper() and s[i+1].islower():
            counter += 1
    return counter
