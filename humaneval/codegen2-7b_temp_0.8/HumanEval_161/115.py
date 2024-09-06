
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
    s_out = ""
    for i in range(len(s)):
        if ord('a') <= ord(s[i]) <= ord('z'):
            s_out += chr(ord(s[i]) - 32)
        else:
            s_out += s[i]
    if len(s_out) == 0:
        s_out = " "
    return s_out
