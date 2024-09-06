
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
    s_lower = [i.lower() if i.isalpha() else i for i in s]
    if any(c.isalpha() for c in s_lower):
        s_upper = [c.upper() if c.isalpha() else c for c in s_lower]
        result = "".join(s_upper)
    else:
        result = "".join(s_lower)
    return result
