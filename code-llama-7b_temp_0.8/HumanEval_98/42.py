
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Count the number of vowels in even-indexed positions.
    # The number of uppercase vowels is equal to the number of vowels in
    # even-indexed positions.

    # Count the number of vowels in even-indexed positions.
    vowels = 'aeiou'
    count = 0
    for i in range(0, len(s), 2):
        if s[i].lower() in vowels:
            count += 1
    return count
