
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # check for invalid input
    if not s or not isinstance(s, str):
        return 0
    # count upper vowels in even indices
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in ['A', 'E', 'I', 'O', 'U']:
            count += 1
    return count
