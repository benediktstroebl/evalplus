
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
    if len([x for x in s if x.isalpha()]) == 0:
        return s[::-1]
    
    res = ""
    for ch in s:
        if ch.isalpha():
            if ch.isupper():
                res += ch.lower()
            else:
                res += ch.upper()
        else:
            res += ch
    return res
