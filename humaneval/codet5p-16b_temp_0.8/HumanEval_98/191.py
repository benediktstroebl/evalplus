
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i, letter in enumerate(s):
        if letter.isupper() and i%2==0:
            count += 1
    return count
