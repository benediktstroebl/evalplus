
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    vowels = 'aeiouAEIOU'
    upper_vowels = [vowel for vowel in vowels if vowel.isupper()]
    count = 0
    for index, char in enumerate(s):
        if index % 2 == 0 and char in upper_vowels:
            count += 1
    return count
