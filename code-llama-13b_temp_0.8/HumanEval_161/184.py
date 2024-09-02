
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
    s = list(s)
    if not s.__contains__(chr(x for x in range(97,123))):
        s.reverse()
        return ''.join(s)
    
    for x in range(len(s)):
        if s[x].isalpha():
            if s[x].islower():
                s[x] = s[x].upper()
            else:
                s[x] = s[x].lower()
        else:
            pass
    
    return ''.join(s)


