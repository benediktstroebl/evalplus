
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
        return ""
    new_s = ""
    res = ""
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].isupper():
                new_s += s[i].lower()
            else:
                new_s += s[i].upper()
        else:
            new_s += s[i]
    for i in range(len(new_s)-1, -1, -1):
        res += new_s[i]
    return res
