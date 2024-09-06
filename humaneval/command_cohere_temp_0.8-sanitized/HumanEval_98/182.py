def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Using list to match indices before and after slicing
    # [0, 2, 4, 6, ...] for even indices
    # [1, 3, 5, 7, ...] for odd indices
    even = [i for i in range(0, len(s), 2)]
    odd = [i for i in range(1, len(s), 2)]
    # Filtering out uppercase vowels from even indices
    result = sum(1 for char in s[even] if char in 'AEU')
    # Checking if there are odd indices remaining after filtering even indices
    return result if len(odd) == 0 else 0