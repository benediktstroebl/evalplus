
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    """
    count_upper(s):
        upper_count = 0
        s_len = len(s)
        for index in range(0, s_len, 2):
            char = s[index]
            if char.isupper() and char in 'AEIOU':
                upper_count += 1
        return upper_count
    """
    return sum(1 for i in range(0, len(s), 2) if s[i].isupper() and s[i] in 'AEIOU')

