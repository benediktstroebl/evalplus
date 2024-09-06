
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Replace all lowercase vowels with a placeholder symbol
    s = s.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')
    # Split the string into a list of substrings
    n = len(s)
    result = 0
    for i in range(n/2):
        # Count the number of uppercase vowels in this substring
        result += sum([1 for x in s[i:(i+1)] if x.isupper()])
    return result
