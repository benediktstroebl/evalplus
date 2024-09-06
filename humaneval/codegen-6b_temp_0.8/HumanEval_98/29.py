
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    
    # Your code here
    
    # This is a very ugly way of counting the vowels.  
    # Python has a built in function that is easy to use though.
    # Count is returning the number of vowels in the string.
    # Must be careful when counting, "ABC" will count as an individual vowel,
    #  while "aBc" will count as 2 vowels.
    # I'm also assuming that vowels are in pairs, so only one vowel will count
    # as one vowel.  
    
    # This is an optimization for counting vowels in even indices.
    # Note: same as asking "how many vowels are there in the string?"
    # -- Will also be useful in the next problem.  
    
    count = 0
    for i in range(0,len(s),2):
        if s[i] in 'AEIOU':
            count += 1
    return count
