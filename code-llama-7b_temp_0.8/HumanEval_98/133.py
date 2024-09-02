
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    vowel = ['A', 'E', 'I', 'O', 'U']
    count = 0
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i].upper() in vowel:
                count += 1
    return count
