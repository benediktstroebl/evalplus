
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    return sum(1 if chr(i).isupper() else 0 for i in range(97, 123) if s[i % len(s)].lower() == chr(i))
