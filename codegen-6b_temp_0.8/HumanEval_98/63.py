
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Your code goes here
    if len(s) == 0:
        return 0
    if len(s) == 1:
        if s.islower():
            return 1
        else:
            return 0
    
    all_vowels = "aeiouAEIOU"
    lower_s = s.lower()
    count = 0
    for i in range(len(lower_s)):
        if lower_s[i] in all_vowels:
            count+=1
        if i%2 !=0:
            continue
    return count
