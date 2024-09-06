
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    if len(s) == 0:
        return 0
    else:
        vowel_count = 0
        for i in range(len(s)):
            if s[i].isupper() and i % 2 == 0:
                vowel_count += 1
        return vowel_count
