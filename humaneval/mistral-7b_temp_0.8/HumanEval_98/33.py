
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    count = 0
    for i in s:
        if (i == "A" or i == "E" or i == "I" or i == "O" or i == "U") and (i in s[0:len(s):2]):
            count += 1
    return count
