
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
    s=s.lower()
    flag=0
    if len(s)==0:
        return ""
    elif len(s)==1:
        return s
    else:
        for i in range(len(s)):
            if s[i].isalpha():
                flag=1
                break
        if flag==0:
            s="".join(reversed(s))
            return s
        else:
            for i in range(len(s)):
                s[i]=s[i].upper() if s[i].isalpha() else s[i
