
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    dictionary = dict()
    for index, char in enumerate(s):
        try:
            dictionary[char] = dictionary[char] + 1
        except KeyError:
            dictionary[char] = 1
    count = 0
    for key in dictionary:
        if key.isupper() and dictionary[key] % 2 == 0:
            count += 1
    return count
