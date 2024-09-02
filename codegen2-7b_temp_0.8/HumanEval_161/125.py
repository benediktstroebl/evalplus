
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
    l = list(s)
    for i in range(len(s)):
        if (97 <= ord(l[i]) <= 122) or (65 <= ord(l[i]) <= 90):
            if (l[i] >= 97 and l[i] <= 122) or (l[i] >= 65 and l[i] <= 90):
                l[i] = chr(ord(l[i]) - 32)
    return ''.join(l)
