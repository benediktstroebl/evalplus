
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
    
    s_rev = ''
    
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].isupper():
                s_rev += s[i].lower()
            elif s[i].islower():
                s_rev += s[i].upper()
            else:
                s_rev += s[i]
        else:
            s_rev += s[i]
            
    return s_rev
