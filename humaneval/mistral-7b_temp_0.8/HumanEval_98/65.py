
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    count = 0
    s_list = list(s)
    for i in range(len(s_list)):
        if i % 2 == 0:
            if s_list[i].isupper() and s_list[i].lower() in ['a', 'e', 'i', 'o', 'u']:
                count += 1
    return count


