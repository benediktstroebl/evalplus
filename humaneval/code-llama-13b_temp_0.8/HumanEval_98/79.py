
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # set up counter
    count = 0
    # check for uppercase letters and vowels
    for i in range(0, len(s)):
        if i % 2 == 0 and s[i].isupper() and s[i] == 'A' or 'E' or 'I' or 'O' or 'U':
            count += 1
    return count
    
