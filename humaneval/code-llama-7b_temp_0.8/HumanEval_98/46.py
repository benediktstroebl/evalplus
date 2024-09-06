
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # check input is string
    if not isinstance(s, str):
        raise TypeError("Input is not a string")
    
    count = 0
    # check if input is empty
    if s == "":
        return count
    
    # count number of uppercase vowels in even indices
    for i in range(len(s)):
        if s[i].isupper() and s[i] in "AEIOU" and i % 2 == 0:
            count += 1
            
    return count
    
