
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # convert to a list of integers
    l = [int(c) for c in s]
    # count the number of odd and even indices
    # for odd indices, the vowel is 'a'
    # for even indices, the vowel is 'b', 'c', 'd', 'e', 'f', 'g'
    odd_count = 0
    even_count = 0
    for i in range(len(l)):
        if i % 2 == 1:
            odd_count += 1
        else:
            even_count += 1
    return odd_count
