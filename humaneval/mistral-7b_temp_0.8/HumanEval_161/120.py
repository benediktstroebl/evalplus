
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
    c = 0
    s1 = ""
    for i in range(len(s)):
        if ord('A') <= ord(s[i]) <= ord('Z') or ord('a') <= ord(s[i]) <= ord('z'):
            if ord(s[i]) >= ord('a') and ord(s[i]) <= ord('z'):
                s1 += chr(ord(s[i]) - 32)
            else:
                s1 += chr(ord(s[i]) + 32)
        else:
            s1 += s[i]
    return s1
