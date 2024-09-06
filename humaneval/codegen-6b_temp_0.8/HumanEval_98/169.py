
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # for loop through the string
    # for each iteration, check the index modulo 2, and add to dictionary if is upper
    # finally return the result
    upper_dict = {}
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i].isupper():
                if s[i].upper() not in upper_dict:
                    upper_dict[s[i].upper()] = 1
                else:
                    upper_dict[s[i].upper()] += 1
    return upper_dict