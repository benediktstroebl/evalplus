
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    return s.upper().count('A')+s.upper().count('E')+s.upper().count('I')+s.upper().count('O')+s.upper().count('U')





