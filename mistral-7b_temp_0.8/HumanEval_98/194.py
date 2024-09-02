
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    g=0
    h=0
    for i in range(0,len(s)):
        if s[i]=='A':
            a+=1
        elif s[i]=='B':
            b+=1
        elif s[i]=='C':
            c+=1
        elif s[i]=='D':
            d+=1
        elif s[i]=='E':
            e+=1
        elif s[i]=='F':
            f+=1
        elif s[i]=='G':
            g+=1
        elif s[i]=='H':
            h+=1
    if a%2==0 and b%2==0 and c%2==0 and d%2==0 and e%2==0 and f%2==0 and g%2==0 and h%2==0:
        return a+b+c+d+e+f+g+h
    else:
        return
