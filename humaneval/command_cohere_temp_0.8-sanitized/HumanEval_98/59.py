def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Using list and subtracting final length by 2 to only consider every second index
    even = [i for i, char in enumerate(s) if char.isupper() and char in 'AEIOU' and i % 2 == 0]
    return len(even)