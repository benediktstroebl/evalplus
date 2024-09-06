
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # FILL IN YOUR CODE HERE
    if (len(s) == 0):
        return 0
    else:
        if s[0] == s[0].upper() and s[0] in 'AEIOU':
            return 1 + count_upper(s[1:])
        else:
            return count_upper(s[1:])

