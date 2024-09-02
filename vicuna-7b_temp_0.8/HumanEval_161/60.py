
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
    dp = 0
    s = s.lower()
    for i in range(len(s)):
        if s[i] in string.ascii_uppercase:
            dp = dp * 2 + 1
        elif s[i] in string.ascii_lowercase:
            dp = dp * 2 + 2
        else:
            dp = dp * 4 + 0
        s = s[:i] + s[i+1:]
    return dp * 2 ** len(s)
