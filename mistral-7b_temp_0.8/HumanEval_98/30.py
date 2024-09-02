
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    vowels = ["A", "E", "I", "O", "U"]
    res = 0
    for i, char in enumerate(s):
        if i % 2 == 0:
            if char.upper() in vowels:
                res += 1
    return res
