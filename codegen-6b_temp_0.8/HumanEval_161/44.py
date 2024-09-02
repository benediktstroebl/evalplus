
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
    return ''.join(s[::-1].split('#')) + '#' + ''.join(s[::-1].split('@')[::-1]) if s.replace('#', '').replace('@', '') else s[::-1]

assert solve("1234") == "4321"
assert solve("ab") == "AB"
assert solve("#a@C") == "#A@c"
assert solve("$#") == "##"
assert solve("") == ""
assert solve("#@$") == "#@$"
