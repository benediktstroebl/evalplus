
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
    if len(s) == 0:
        return s
    if len(s) == 1:
        if s.isalpha():
            return s.upper()
        return s.lower()
    if s[0].isalpha():
        return solve(s[1:]) + s[0].upper() + solve(s[1:])
    return solve(s[1:]) + s[0].lower() + solve(s[1:])

