
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    
    # #Thoughts:
    # do the even indices when counting vowels?
    # do the odd indices, when counting vowels?
    # is the first index a letter?
    
    # we've broken down to two cases:
    # count_upper_vowel_even or count_upper_vowel_odd
    
    # Could also be done with a one-liner:
    # return sum(1 for c in s[::2] if c.isupper())
        
    # But first, we need to translate the s to a list
    # so that we can use a list comprehension
    s = list(s)
    
    #The second 'if' statement basically says about the case when the list starts with a letter
    #We don't want to include that here because we want the count_upper_vowel_even situation
    if s[0].isupper():
        #So, we want the even indices
        return sum(1 for c in s[1::2] if c in VOWELS)
    else:
        #So, we want the odd indices
        return sum(1 for c in s[1::2] if c in VOWELS)
