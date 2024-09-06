def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Use a dictionary to store the counts of uppercase vowels ('A', 'E', 'I', 'O', 'U')
    vowel_counts = {char: 0 for char in 'AEIOU'}
    total_count = 0
    
    # Iterate through the string
    for i, char in enumerate(s):
        if char.isupper() and char in vowel_counts and i % 2 == 0:
            vowel_counts[char] += 1
            total_count += 1
    
    return total_count