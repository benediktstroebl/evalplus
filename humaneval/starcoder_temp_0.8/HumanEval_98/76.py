
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Your code here.
    count=0
    for i in s:
        if i in ['a','e','i','o','u']:
            count+=1
        if i in ['A','E','I','O','U']:
            if (s.index(i)%2)==0:
                count+=1
    return count
