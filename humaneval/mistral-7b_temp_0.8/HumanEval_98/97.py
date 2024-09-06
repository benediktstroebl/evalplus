
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    #s=s.upper()
    #print(s)
    #print(len(s))
    #for i in range(len(s)):
    #    if s[i] in 'ABCDE':
    #        if i%2==0:
    #            print(s[i])
    #            print(i)
    #            count+=1
    #return count
    return s.count("A")+s.count("B")+s.count("C")+s.count("D")+s.count("E")+s.count("F")+s.count("G")

