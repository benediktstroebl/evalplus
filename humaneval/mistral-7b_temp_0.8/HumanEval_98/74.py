
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    vowel_list = ['A','a','E','e','I','i','O','o','U','u']
    vowel_count = 0
    for i in range(len(s)):
        if s[i].upper() in vowel_list and i%2==0:
            vowel_count += 1

    return vowel_count

