
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
        if l[i].isalpha():
            if l[i].isupper():
                l[i] = l[i].lower()
            else:
                l[i] = l[i].upper()
    return "".join(l)
