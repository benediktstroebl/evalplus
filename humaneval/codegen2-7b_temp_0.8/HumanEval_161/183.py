
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
    chars = list(s)
    for i, c in enumerate(chars):
        if c.isalpha():
            chars[i] = chr(ord(c) ^ (1 << 5))
    return "".join(chars)

