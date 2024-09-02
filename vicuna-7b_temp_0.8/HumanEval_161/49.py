
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
    if not s:
        return "#" + s[::-1]
    l = len(s)
    rev_s = ""
    for i in range(l):
        if s[i].isalpha():
            rev_s += s[i].upper()[::-1]
            if i < l - 1:
                rev_s += s[i+1]
        else:
            rev_s += s[i]
    return "".join(reversed(rev_s))
