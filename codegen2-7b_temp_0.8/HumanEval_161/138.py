
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
    
    if len(s) == 1:
        return s.lower() if s.isupper() else s.upper()
    
    res = ""
    for i in range(len(s)-1):
        res += chr(s[i]) if s[i].isalpha() else s[i]
    
    res += s[-1].upper() if s[-1].isalpha() else s[-1].lower()
    
    return
