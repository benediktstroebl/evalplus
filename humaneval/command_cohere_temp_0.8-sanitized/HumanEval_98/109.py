def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    upper_vowels = {"A":1, "E":1, "I":1, "O":1, "U":1}
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in upper_vowels and s[i].isupper():
            count += 1
    return count