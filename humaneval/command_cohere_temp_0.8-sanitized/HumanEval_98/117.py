def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    LC = s.lower()
    return sum(1 for i, char in enumerate(LC) if i % 2 == 0 and char in 'AEIOU' and char == s[i].upper())