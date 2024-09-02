
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
    i = 0
    while i < len(l):
        if l[i].isalpha():
            if l[i].islower():
                l[i] = l[i].upper()
            else:
                l[i] = l[i].lower()
        i += 1
    return ''.join(l)
