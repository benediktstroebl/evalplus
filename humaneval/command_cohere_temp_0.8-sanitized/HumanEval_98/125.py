def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Ensure the string contains only uppercase vowels and consonants
    vowels = set('AEIOU')
    if not all(c in vowels or c.isalpha() for c in s):
        return 'Invalid input. String should only contain uppercase vowels and consonants.'
    
    # Count uppercase vowels in even indices.
    return sum(1 for i in range(0, len(s), 2) if s[i] in vowels)