
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Your code here
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ans = 0
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] in lowercase:
                if s[i].upper() in uppercase:
                    ans += 1
    return ans
