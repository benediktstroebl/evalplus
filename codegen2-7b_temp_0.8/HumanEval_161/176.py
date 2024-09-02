
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
    c=0
    for i in range(len(s)):
        if s[i].isalpha():
            c=1
            if s[i].islower():
                s[i]=chr(ord(s[i])-32)
            else:
                s[i]=chr(ord(s[i])+32)
        else:
            s[i]=s[i]
    if c==0:
        return "".join(s)
    return "".join(
