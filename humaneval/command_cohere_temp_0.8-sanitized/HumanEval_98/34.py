def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Use a dictionary to store the number of uppercase vowels in even indices.
    # Initialize it to 0 initially.
    count = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    even_indices = [i for i, char in enumerate(s) if (i % 2 == 0 and char.isupper() and char in vowels)]
    count = sum(1 for _ in even_indices)
    return count