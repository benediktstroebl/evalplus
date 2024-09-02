
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
    new_s=[]
    for i in range(0,len(s)):
        if(s[i].isalpha()):
            if(s[i].islower()):
                new_s.append(s[i].upper())
            else:
                new_s.append(s[i].lower())
        else:
            new_s.append(s[i])
    return "".join(new_s)
