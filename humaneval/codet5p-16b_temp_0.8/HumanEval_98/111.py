
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    num_vowels = 0
    i = 0
    while i < len(s):
        if s[i].isupper():
            if i % 2 == 0:
                num_vowels += 1
        i += 1
    return num_vowels

