
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    upper_count = 0
    for idx, letter in enumerate(s):
        if idx % 2 == 0:
            if letter.isupper():
                upper_count += 1
    return upper_count

