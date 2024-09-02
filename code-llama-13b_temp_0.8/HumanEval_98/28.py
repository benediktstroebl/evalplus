
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # 1st Solution:
    count = 0
    for i in range(len(s)):
        if s[i].isupper() and s[i] in 'AEIOU' and i%2==0:
            count += 1
    return count
    
    # 2nd Solution:
    count = 0
    for i in range(0,len(s),2):
        if s[i].isupper() and s[i] in 'AEIOU':
            count += 1
    return count
    
    # 3rd Solution:
    count = 0
    for i in range(len(s)):
        if s[i].isupper() and s[i] in 'AEIOU' and i%2==0:
            count += 1
    return count
    
    # 4th Solution:
    return sum([s[i].isupper() and s[i] in 'AEIOU' for i in range(0,len(s),2)])
    
    
    
