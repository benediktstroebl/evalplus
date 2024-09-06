
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    vowels = 'AEIOU'
    
    num_vowels = 0
    
    for i in range(0, len(s), 2):
        num_vowels += sum(1 for c in s[i] if c in vowels)
        
    return num_vowels
    
