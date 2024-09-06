
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
    if n==0:
        return ""
    if s[0].isupper():
        s=s.lower()
    elif s[0].islower():
        s=s.upper()
    else:
        return s
    return s[::-1]
