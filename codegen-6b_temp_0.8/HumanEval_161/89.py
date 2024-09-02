
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
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@".upper()
    ret = []
    for c in s:
        if c.upper() in letters:
            ret.append(c.upper() if c.isdigit() else c)
        elif c.lower() in letters:
            ret.append(c.lower() if c.isdigit() else c)
    return "".join(ret)

