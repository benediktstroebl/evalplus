
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # a better version (without for loop) is to use list comprehension
    # a = [i for i in s if i in UPPERCASE and s[i] in EVEN_INDICES]
    # return len(a)
    count = 0
    for i in range(len(s)):
        if s[i] in UPPERCASE and s[i] in EVEN_INDICES:
            count += 1
    return count
