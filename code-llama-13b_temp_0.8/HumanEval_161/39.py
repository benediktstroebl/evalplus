
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
    
    if not s:
        return ""
    
    l = len(s)
    t = 0
    
    for i in range(0,l):
        if s[i].isalpha():
            t = 1
            break
    
    if t == 0:
        return s[::-1]
    
    new_s = ""
    for i in range(0,l):
        if s[i].isalpha():
            if s[i].islower():
                new_s += s[i].upper()
            else:
                new_s += s[i].lower()
        else:
            new_s += s[i]
    return new_s
