
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
    for s1 in s:
        if s1.isalpha():
            if s1.islower():
                res += s1.upper()
            else:
                res += s1.lower()
        else:
            res += s1
    if len(res) == 0:
        return s[::-1]
    return res

