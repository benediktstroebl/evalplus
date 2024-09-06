
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
        return ""
    if len(s) == 1:
        return s[0].lower() if s[0].isalpha() else s[0]

    if not (s[0].isalpha() or s[0].isdigit()):
        return solve(s[1:]) + solve(s[0])

    char = s[0]
    if char.isalpha():
        return solve(s[1:]) + char.lower()
    else:
        return solve(s[1:]) + char.upper()

