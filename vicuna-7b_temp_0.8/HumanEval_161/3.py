
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
    s = s.lower()
    i = 0
    cnt = 0
    while i < len(s):
        if s[i].isalnum():
            if s[i] == s[i].upper():
                s = s[:i] + s[i].lower() + s[i+1:]
                cnt += 1
            else:
                s = s[:i] + s[i].upper() + s[i+1:]
                cnt += 1
        else:
            cnt += 1
        i += 1
    if cnt > 0:
        s = s.title()
    return s
