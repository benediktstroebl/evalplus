
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Your code here
    count = 0
    i = 0
    for ch in s:
        if i % 2 == 0 and ch.isupper():
            count += 1
        i += 1
    return count
