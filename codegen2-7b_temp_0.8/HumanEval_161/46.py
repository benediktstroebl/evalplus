
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
    res = ""
    for i in range(len(s)):
        if s[i].islower():
            res = res + s[i].upper()
        elif s[i].isupper():
            res = res + s[i].lower()
        else:
            res = res + s[i]
    if not res:
        return res
    return res[::-1]
    
