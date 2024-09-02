
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    result = 0
    for index, value in enumerate(s):
        if index % 2 == 0 and value.isupper() and value in 'AEIOU':
            result += 1
    return result
    
    pass
    # your code here






