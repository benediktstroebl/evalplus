
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
    r = ""
    if s == "":
        return s
    for i in range(len(s)):
        if ord(s[i]) >= ord("a") and ord(s[i]) <= ord("z"):
            r += chr(ord(s[i]) - 32)
        else:
            r += s[i]
    return r

