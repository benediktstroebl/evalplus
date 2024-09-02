
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
    if s == "":
        return s
    if s[0].isalpha():
        return s[0].upper() + solve(s[1:])
    elif s[0].isdigit():
        return s[0] + solve(s[1:])
    else:
        return solve(s[1:])
