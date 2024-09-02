
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
    s = s.upper()
    d = {}
    for i, c in enumerate(s):
        if c.isalpha():
            if c.islower():
                d[i] = chr(ord(c) - ord('a') + ord('A'))
            else:
                d[i] = chr(ord(c) - ord('A') + ord('a'))
        else:
            d[i] = c
    return ''.join(d)

s = input()
result = solve(s)
