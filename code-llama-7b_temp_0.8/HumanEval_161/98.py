
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
    n=len(s)
    for i in range(n):
        if s[i].isalpha():
            if s[i].islower():
                s=s[:i]+s[i].upper()+s[i+1:]
            else:
                s=s[:i]+s[i].lower()+s[i+1:]
    if not any(c.isalpha() for c in s):
        s=s[::-1]
    return s

    
