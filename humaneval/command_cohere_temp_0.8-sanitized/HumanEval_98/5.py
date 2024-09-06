def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Ensure the string has an even length to handle the edge case where the last character is a vowel
    s += s if len(s) % 2 else 'x'
    return sum(1 for char in s if char.isupper() and char in 'AEIOU') // 2