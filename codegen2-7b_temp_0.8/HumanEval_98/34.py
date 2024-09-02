
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    count = 0
    for char in s:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            count += 1
            if count % 2 == 0:
                return count
        count += 1
    
