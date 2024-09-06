
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # YOUR CODE HERE
    upper_vowels = ['A', 'E', 'I', 'O', 'U']
    counter = 0
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] in upper_vowels:
                counter += 1
    return counter
