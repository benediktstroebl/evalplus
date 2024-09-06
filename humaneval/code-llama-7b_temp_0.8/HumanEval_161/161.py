
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
    if s == None: return
    result = ''
    for c in s:
        if c.isalpha():
            if c.isupper():
                result = result + c.lower()
            else:
                result = result + c.upper()
        else:
            result = result + c
    if len(result) == 0:
        return s[::-1]
    else:
        return result
