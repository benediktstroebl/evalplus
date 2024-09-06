
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # use a dictionary to count the number of vowels
    vowels = {char.upper(): 0 for char in s}
    for i in range(1, len(s)):
        if s[i] == s[i-1].upper():
            vowels[s[i].upper()] += 1
    return vowels
