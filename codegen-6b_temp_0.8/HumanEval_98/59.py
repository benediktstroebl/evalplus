
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    return sum(s[i].isupper() and s[i].isalpha() for i in range(1, len(s), 2))

    """
    # Solution:
    vowels = set('aeiou')
    count = 0
    for index, letter in enumerate(s):
        if letter.isalpha() and index % 2 == 0:
            if letter.lower() in vowels:
                count += 1
    return count
    """
