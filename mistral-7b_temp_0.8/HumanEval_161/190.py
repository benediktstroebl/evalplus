
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
    s = s.translate(str.maketrans("","", "1234567890"))
    s = s.translate(str.maketrans("","", "abcdefghijklmnopqrstuvwxyz"))
    s = s.translate(str.maketrans("","", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    s = s.lower()
    if not s:
        return ""
    return s[::-1]
