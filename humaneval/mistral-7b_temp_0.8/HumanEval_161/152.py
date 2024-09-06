
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
    s1 = ""
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].islower():
                s1 += s[i].upper()
            else:
                s1 += s[i].lower()
        else:
            s1 += s[i]
    return s1

