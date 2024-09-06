
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
    s = s.lower()
    if not s:
        return s
    s = s.split("")
    if s[0] in "abcdefghijklmnopqrstuvwxyz":
        for i in range(0,len(s)):
            s[i] = s[i].swapcase()
    return ''.join(s)

