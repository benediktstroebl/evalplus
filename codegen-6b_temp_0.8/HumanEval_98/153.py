
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    vowels = ['A', 'E', 'I', 'O', 'U']
    return sum(s[i] in vowels and i%2 == 0 for i in range(len(s)))
    
    # another way:
    # return sum(s[i].isupper() for i in range(0, len(s), 2))
