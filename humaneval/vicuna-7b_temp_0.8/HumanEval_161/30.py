
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
    s_lower = ""
    s_upper = ""
    i = 0
    while i < len(s):
        if s[i].isalpha():
            if s[i].islower():
                s_upper += s[i].upper()
            else:
                s_lower += s[i].lower()
        elif s[i] == "#":
            if s[i+1].isalpha():
                s_upper += s[i+1].upper()
            else:
                s_lower += s[i+1].lower()
        else:
            s_upper += s[i]
        i += 1
    return s_upper
