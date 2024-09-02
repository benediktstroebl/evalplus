
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    even = []
    odd = []
    for i in s:
        if s.index(i) % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    for i in even:
        if i.upper() in ('A', 'E', 'I', 'O', 'U'):
            return 1
    return 0
    # return count_upper('dBBE')


