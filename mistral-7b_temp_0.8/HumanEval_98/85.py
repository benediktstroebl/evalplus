
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # This is a bad way to do this.
    # The only thing I did right was to write a helper function.
    # If you wanted to do it this way, you would have to search the string for the even indexed vowels,
    # and then count them.

    # This is a better way to do it.
    # It uses a for loop to iterate through the string, and then it checks if each character is a vowel and
    # if it is in an even index.
    # This way is faster than the other way, because it doesn't have to search the string for the vowels.

    # This is an even better way to do it.
    # It uses a generator expression to create a list of the even indexed vowels, and then it counts them.
    # This way is the fastest, because it doesn't have to search the string for the vowels,
    # and it also doesn't have to iterate through the string.
    return len([c for i,c in enumerate(s) if c.upper() in "AEIOU" and i%
