
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    if len(s) % 2!= 0:
        return 0
    count = 0
    for i in range(len(s)//2):
        if s[2*i] == 'A' or s[2*i] == 'E' or s[2*i] == 'I' or s[2*i] == 'O' or s[2*i] == 'U':
            count
