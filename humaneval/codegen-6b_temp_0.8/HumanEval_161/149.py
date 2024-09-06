
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
    s = s.lower()
    if s.isalpha() is False:
        return s[::-1]
    else:
        return s.swapcase()



assert solve("1234") == "4321"
assert solve("ab") == "AB"
assert solve("#a@C") == "#A@c"