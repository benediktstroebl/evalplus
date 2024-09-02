
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
        return s
    if not any(char.isalpha() for char in s):
        return s[::-1]
    r = ""
    for char in s:
        if char.isalpha():
            r += char.lower() if char.isupper() else char.upper()
        else:
            r += char
    return r

