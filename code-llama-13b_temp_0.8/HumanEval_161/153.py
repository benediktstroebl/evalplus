
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
    if not s: return ""
    res = []
    for i in range(len(s)):
        if not s[i].isalpha(): res.append(s[i])
        else: res.append(s[i].swapcase())
    return "".join(res[::-1]) if not any(i.isalpha() for i in res) else "".join(res)
