
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    if len(s) % 2 != 0:
        return 0
    upper_vowel = 'AEIOU'
    upper_vowel_count = 0
    for each in s[0:len(s)//2]:
        if each in upper_vowel:
            upper_vowel_count += 1
    for each in s[len(s)//2:]:
        if each in upper_vowel:
            upper_vowel_count += 1
    return upper_vowel_count

