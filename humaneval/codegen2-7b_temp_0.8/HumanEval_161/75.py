
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
    for i in range(len(s)-1,-1,-1):
        if s[i] in ['a','e','i','o','u','A','E','I','O','U']:
            s=s[:i]+s[i].upper()+s[i+1:]
        else:
            s=s[:i]+s[i].lower()+s[i+1:]
    return s

