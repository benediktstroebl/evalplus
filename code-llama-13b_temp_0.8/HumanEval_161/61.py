
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
    s_mod = ""
    count = 0
    for x in s:
        if x.isalpha():
            x = x.upper() if x.islower() else x.lower()
            count += 1
        s_mod += x

    return s_mod if count else s[::-1]


