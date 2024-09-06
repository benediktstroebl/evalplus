
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    vowels = "aeiouAEIOU"
    num_vowels = 0
    for index in range(0, len(s), 2):
        if s[index].lower() in vowels:
            num_vowels += 1
    
    return num_vowels
