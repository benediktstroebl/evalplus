
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # count the number of vowels in odd-indexed characters (i.e. the first, third, etc.)
    # note that we start with the first character, which is the zeroth
    count = 0
    for i in range(len(s)):
        if i % 2 == 1:
            if s[i].isupper():
                count += 1
    return count
