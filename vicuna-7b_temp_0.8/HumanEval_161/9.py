
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
    # Not using any string methods
    s = s.lower() # lowercase all letters
    d = {}
    for c in s:
        if c.isalpha():
            d[c.lower()] = c.upper()
        else:
            d[c] = c
    result = ""
    for i, c in enumerate(s):
        if c in d:
            result += d[c].lower()
        else:
            result += c
    return result
