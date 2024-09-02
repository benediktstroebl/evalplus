
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # vowels = ('a', 'e', 'i', 'o', 'u')
    # even_index = [s[i] for i in range(0, len(s), 2)]
    # upper_vowels = [item for item in even_index if item in vowels and item.isupper()]
    # return len(upper_vowels)
    
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in 'AEIOU' and s[i].isupper():
            count += 1
    return count

