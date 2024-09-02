
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    result = 0
    index = 0
    while index < len(s) - 1:
        if s[index].isupper() and s[index+1].isupper():
            result += 1
            index += 2
        else:
            index += 1
    return result

