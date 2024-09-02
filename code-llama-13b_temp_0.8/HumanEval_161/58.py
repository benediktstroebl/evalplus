
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
    r = ''
    s1 = s[::-1]
    for i in range(len(s1)):
        if s1[i].isalpha():
            if s1[i].isupper():
                r = r + s1[i].lower()
            else:
                r = r + s1[i].upper()
        else:
            r = r + s1[i]
    if r.isalpha():
        return r[::-1]
    else:
        return r
