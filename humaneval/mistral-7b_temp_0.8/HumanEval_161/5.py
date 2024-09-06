
def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    """
    # Write your code here
    s=s.lower()
    i=0
    j=len(s)-1
    #print(s)
    while(i<=j):
        if(s[i]>='a' and s[i]<='z'):
            s=s[0:i]+s[i].upper()+s[i+1:j+1]
            i+=1
        else:
            s=s[0:i]+s[i]+s[i+1:j+1]
            i+=1
        j-=1
    return s

