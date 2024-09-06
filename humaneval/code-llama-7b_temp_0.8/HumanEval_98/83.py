
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    #set the counter to 0
    count = 0
    
    #for each character in the string
    for i in range(len(s)):
        #if the character is in the list
        if s[i] in ['A', 'E', 'I', 'O', 'U']:
            #if the index is even
            if i % 2 == 0:
                #add one to the counter
                count += 1
    #return the counter
    return count
