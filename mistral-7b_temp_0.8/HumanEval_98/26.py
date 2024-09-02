
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Your code here
    if s is None:
        return 0
    else:
        if s=='':
            return 0
        else:
            return count_upper(s[1:]) + 1 if s[0].isupper() and s[0].isalpha() and (len(s)%2==0) else count_upper(s[1:])
