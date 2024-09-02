
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # build dictionary of vowels and their counts
    vowels = 'aeiouAEIOU'
    vowel_counts = {}
    for v in vowels:
        vowel_counts[v] = 0
    for char in s:
        if char.isupper():
            if vowel_counts[char]:
                vowel_counts[char] += 1
            else:
                vowel_counts[char] = 1
    return sum(vowel_counts[v] for v in vowels if vowel_counts[v] % 2 == 0)
