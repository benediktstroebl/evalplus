
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
    res = ""
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].isupper():
                res += s[i].lower()
            else:
                res += s[i].upper()
        else:
            res += s[i]
    return res if len(res) > 0 else s[::-1]

