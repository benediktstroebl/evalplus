
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    if len(s) % 2 == 0:
        return len(re.findall('[AEIOU]', s[::2]))
    else:
        return len(re.findall('[AEIOU]', s[::2])) + len(re.findall('[AEIOU]', s[1::2]))
