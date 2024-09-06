
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    VOWELS = "aeiou"
    return sum([len([c for c in s if c in VOWELS and i % 2 == 0]) for i, _ in enumerate(s)])

