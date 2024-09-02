
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Your code here
    #This is the code that I used when I had the time to sit down and work on it
    #However, since I only had a few minutes when I was working on this it didn't work so I
    #had to revert to the code I submitted below.
    #count = 0
    #for i in range(0,len(s),2):
    #    if s[i].isupper():
    #        count += 1
    #return count
    #This is the code that I used when I had more time
    count = 0
    for i in range(0, len(s),2):
        if s[i].isupper():
            count += 1
    return count



