
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
    n = len(s)
    ans = ""
    for i in range(n):
        if s[i].isalpha():
            if s[i].islower():
                ans += s[i].upper()
            else:
                ans += s[i].lower()
        else:
            ans += s[i]
    return ans
