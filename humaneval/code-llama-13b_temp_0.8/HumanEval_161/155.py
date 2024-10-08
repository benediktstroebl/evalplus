
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
    letters = False
    result = ""
    for c in s:
        if c.isalpha():
            letters = True
        if c.isalpha():
            result += c.lower() if c.isupper() else c.upper()
        else:
            result += c

    if not letters:
        result = result[::-1]

    return result
