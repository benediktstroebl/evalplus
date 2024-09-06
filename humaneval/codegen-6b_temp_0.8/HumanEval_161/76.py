
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
    return ''.join(map(lambda x: x*-1 if x in string.ascii_letters else x, s))[::-1]

assert solve("ab") == "AB"
assert solve("1234") == "4321"
assert solve("#a@C") == "#A@c"
assert solve("1234ab") == "4321ab"
