
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
    for i in range(len(s)):
        if ord(s[i]) > 64 and ord(s[i]) < 91:
            s = s[:i] + s[i].lower() + s[i+1:]
        elif ord(s[i]) > 96 and ord(s[i]) < 123:
            s = s[:i] + s[i].upper() + s[i+1:]
        else:
            continue
    return s[::-1] if s.isnumeric() else s

