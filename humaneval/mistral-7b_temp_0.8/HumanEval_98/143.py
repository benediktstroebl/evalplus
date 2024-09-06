
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    vowels = 'AEIOUaeiou'
    upper_vowels = 'AEIOU'

    s = s.lower()
    result = 0
    for i, c in enumerate(s):
        if i % 2 == 0:
            if c in upper_vowels:
                result += 1
    return result

