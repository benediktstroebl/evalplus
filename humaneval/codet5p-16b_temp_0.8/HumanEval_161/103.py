
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

    is_letter = lambda x: x.isalpha()
    is_lower = lambda x: x.islower()
    is_upper = lambda x: x.isupper()
    if is_letter(s):
        if is_lower(s):
            return s.upper()
        if is_upper(s):
            return s.lower()
    else:
        return s[::-1]
