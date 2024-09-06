
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # my_solution
    up_vowels = ['A', 'E', 'I', 'O', 'U']
    count = 0
    for i in range(len(s)):
        if i%2 == 0 and s[i] in up_vowels:
            count += 1
    return count
