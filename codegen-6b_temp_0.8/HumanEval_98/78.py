
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Hint: you may find the built-in .count() method to be useful
    
    count = 0
    for i in range(1, len(s), 2):
        if s[i].isupper():
            count += 1
    return count
