
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    even = []
    for i in range(len(s)):
        if i % 2 == 0:
            even.append(s[i])
    count = 0
    for x in even:
        if x.upper() in vowels:
            count += 1
    return count
