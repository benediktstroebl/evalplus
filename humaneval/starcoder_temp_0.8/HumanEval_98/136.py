
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    vowels = ('A', 'E', 'I', 'O', 'U')
    count = 0
    for index, letter in enumerate(s):
        if letter in vowels and index % 2 == 0:
            count += 1
    return count

