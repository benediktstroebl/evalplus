
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    
    # 1. check for empty string
    if len(s) == 0:
        return 0
    
    # 2. check first character is uppercase vowel
    if s[0] in 'AEIOU' and s[0].isupper():
        # if True, increase count by 1
        count = 1
    else:
        # if False, set count to zero
        count = 0
    
    # 3. iterate over string to find other uppercase vowels
    for char in s[1::2]:
        # check if character is uppercase vowel
        if char in 'AEIOU' and char.isupper():
            count += 1
    
    return count

