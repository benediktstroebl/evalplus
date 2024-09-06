
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Convert the string to a list of characters
    words = [s]
    for i in range(len(s)):
        if s[i].isupper():
            words.append(s[i+1:])
            i += 1
    return len(set(words) - set(['']))
