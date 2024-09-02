
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
    def helper(s):
        if s == "":
            return ""
        if s[0].isupper():
            return helper(s[1:])
        if s[0].islower():
            return s[0].upper() + helper(s[1:])
        return s

    return helper(s)

