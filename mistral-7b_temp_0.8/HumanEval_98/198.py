
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # your code goes here
    # print(s)
    count=0
    for i in range(len(s)):
        if i%2==0:
            if (s[i].upper()=='A' or s[i].upper()=='E' or s[i].upper()=='I' or s[i].upper()=='O' or s[i].upper()=='U'):
                count+=1
    return count

