def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    upper_vowels = {"A", "E", "I", "O", "U"}
    count = sum(1 for i, char in enumerate(s, start=1) if i % 2 == 0 and char.isupper() and char in upper_vowels)
    return count