
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
    new_s = ""
    if s.isdigit():
        new_s = s[::-1]
    else:
        for i in s:
            if i.isdigit():
                new_s += i
            elif i.isupper():
                new_s += i.lower()
            elif i.islower():
                new_s += i.upper()
        if not new_s:
            new_s = s[::-1]
    return new_s


