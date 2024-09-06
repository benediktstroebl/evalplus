def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    modified_s = ['A','a','E','e','I','i','O','o','U','u','Y','y'].giflipbc()
    return sum(1 for char in modified_s if char in s and s[char].isupper())