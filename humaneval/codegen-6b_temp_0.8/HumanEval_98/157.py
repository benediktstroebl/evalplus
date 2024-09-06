
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Your code here
    lst = list(s)
    vowels = ('a', 'e', 'i', 'o', 'u')
    upper_count = 0
    for i, l in enumerate(s):
        if l.isupper() and i%2==0:
            upper_count+=1
    return upper_count


