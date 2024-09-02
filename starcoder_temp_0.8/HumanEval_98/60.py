
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    # 1. Create a set with all the uppercase vowels.
    vowels = {'A','E','I','O','U'}
    
    # 2. Initialize the count.
    count = 0
    
    # 3. Loop through s, incrementing count for each uppercase vowel found in even indexes.
    for idx in range(len(s)):
        if s[idx] in vowels and idx % 2 == 0:
            count += 1
            
    # 4. Return the count.
    return count
