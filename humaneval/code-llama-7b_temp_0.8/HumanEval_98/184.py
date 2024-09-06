
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    #for letter in s:
    #    if letter in 'AEIOU':
    #        #check whether the index is even
    #        return s[0::2].count(letter.upper())
    #return 0

    return len([letter for letter in s[0::2] if letter in 'AEIOU'])
