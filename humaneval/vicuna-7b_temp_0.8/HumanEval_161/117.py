
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
    d = {}
    for c in s:
        if c.isalpha():
            if c.lower() in d:
                d[c.lower()] = d[c.lower()] + 1
            else:
                d[c.upper()] = 1
                d[c.lower()] = 1
        elif c.isdigit():
            d[str(c)] = 1
    result = ''
    for k, v in d.items():
        if v == 1:
            result += k.upper()
        elif v == 2:
            result += k.lower()
    return result
