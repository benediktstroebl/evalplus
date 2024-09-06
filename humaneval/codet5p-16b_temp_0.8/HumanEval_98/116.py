
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    vowels = 'AEIOU'
    even_indices = [i for i in range(len(s)) if i % 2 == 0]
    result = 0
    for i in even_indices:
        if s[i] in vowels:
            result += 1
    return result
