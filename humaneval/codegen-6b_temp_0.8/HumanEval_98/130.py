
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    vowel_values = [ord('A'), ord('E'), ord('I'), ord('O'), ord('U')]
    num_vowels = 0
    for i in range(0, len(s), 2):
        if ord(s[i]) in vowel_values:
            num_vowels += 1
    return num_vowels
    