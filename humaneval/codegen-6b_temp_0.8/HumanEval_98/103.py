
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Hint: use s[i] == s[len(s)-1-i] to check if the ith character is uppercase
    counter = 0
    for i in xrange(len(s)):
        if s[i].isupper():
            if i % 2 == 0:
                counter += 1
    return counter
    