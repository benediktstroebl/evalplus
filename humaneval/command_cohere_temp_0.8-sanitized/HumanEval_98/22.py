def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    Example:
    >>> count_upper('aBCdEf')
    1
    >>> count_upper('abcdefg')
    0
    >>> count_upper('dBBE')
    0
    """
    # Use a dictionary to store the count of each vowel
    vowel_count = { 'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0 }
    # Iterate through the string
    for i in range(len(s)):
        if i % 2 == 0 and s[i].isupper():
            if s[i] in vowel_count:
                vowel_count[s[i]] += 1
    # Sum the counts and return the result
    return sum(vowel_count.values())