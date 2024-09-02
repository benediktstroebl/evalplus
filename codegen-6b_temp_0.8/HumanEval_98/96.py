
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Hint: Use a two parameter function to count the vowels in a string
    # and return the sums of the vowels in the even indices
    # Example: sum([0,2,4]) returns 1+2+4 = 7
    vowels = 0
    for index in range(0, len(s), 2):
        vowels += Counter(s[index]).get('A',0)
    return vowels
    