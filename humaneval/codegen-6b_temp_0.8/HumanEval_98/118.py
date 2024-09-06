
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    #return sum(s[i].isupper() for i in range(0, len(s), 2))
    #return sum(1 for i in range(0, len(s), 2) if s[i].isupper())
    #return sum(c in ['A','E','I','O','U'] for c in s)
    #return sum(s[i] in ['A','E','I','O','U'] for i in range(0, len(s), 2))
    return sum(c in ['A','E','I','O','U'] for i, c in enumerate(s) if i%2==0)
