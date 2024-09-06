
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # YOUR CODE HERE
    total = 0
    for i in range(0, (len(s) - 1), 2):
        if s[i] > 'A' and s[i].lower() in 'aeiou':
            total += 1
    return total

