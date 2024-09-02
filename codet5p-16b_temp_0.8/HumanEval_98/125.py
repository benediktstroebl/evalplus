
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    upper_vowels = [i for i in s if i.isupper()]
    return sum([1 if i % 2 == 0 else 0 for i in range(len(s))])
