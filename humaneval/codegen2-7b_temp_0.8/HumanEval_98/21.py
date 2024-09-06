
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    s = s.lower()
    count = 0
    for letter in s:
        if ord(letter) >= 65 and ord(letter) <= 90 and s.index(letter)%2 == 0:
            count += 1
    return
