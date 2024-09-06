
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
    n = len(s)
    d = {}
    for i, c in enumerate(s):
        if c.isalpha():
            if c.lower() in d:
                d[c.lower()] = d[c.lower()] + 1
            else:
                d[c.lower()] = 1
            if c.upper() in d:
                d[c.upper()] = d[c.upper()] + 1
            else:
                d[c.upper()] = 1
        elif c.isdigit():
            d[str(c)] = d[str(c)] + 1
    return ''.join([''.join(d[c]) if d[c] > 0 else c for c in s])
