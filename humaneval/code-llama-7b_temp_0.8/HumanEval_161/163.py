
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
    s2 = ''
    for i in range(len(s)):
        if ord(s[i]) in range(65,91):
            s2 += chr(122-(ord(s[i])-65))
        elif ord(s[i]) in range(97,123):
            s2 += chr(64-(ord(s[i])-97))
        else:
            s2 += s[i]
    return s2 if len(s2) else s[::-1]
