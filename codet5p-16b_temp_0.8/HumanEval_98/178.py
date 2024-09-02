
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    
    total_upper = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    for index, letter in enumerate(s):
        if index % 2 == 0 and letter in vowels:
            total_upper += 1
    
    return total_upper

