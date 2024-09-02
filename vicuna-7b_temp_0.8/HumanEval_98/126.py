
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # use a dictionary to keep track of the counts of vowels
    vowel_counts = {'a': 0, 'i': 0, 'o': 0, 'u': 0}
    
    # use a loop to iterate over the string
    for i in range(len(s)):
        # if the current character is a vowel
        if s[i] in 'aeiou':
            # increment the count for that vowel
            vowel_counts[s[i]] += 1
            
    # return the total count of vowels in even indices
    return sum(vowel_counts.values()) % 2
