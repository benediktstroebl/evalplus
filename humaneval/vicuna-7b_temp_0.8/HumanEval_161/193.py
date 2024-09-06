
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
    s = "".join(reversed(s))
    for i in range(len(s)):
        if s[i] in "abcdefghijklmnopqrstuvwxyz":
            s = s[:i] + s[i].upper() + s[i+1:]
        elif s[i] in "0123456789":
            s = s[:i] + s[i].lower() + s[i+1:]
    return s
