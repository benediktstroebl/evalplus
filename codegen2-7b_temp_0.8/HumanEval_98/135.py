
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    counter = 0
    for index in range(0,len(s)):
        if s[index] == 'a' or s[index] == 'A':
            counter += 1
        if s[index] == 'i' or s[index] == 'I':
            counter += 1
    return counter
