
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
    i = 0
    j = len(s) - 1
    ans = ""
    while i <= j:
        if s[i].isalpha():
            ans += s[i].upper() if s[i].islower() else s[i].lower()
        else:
            ans += s[i]
        i += 1

    return ans[::-1]

