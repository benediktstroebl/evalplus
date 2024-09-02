
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
    r = list(s)
    i = 0
    while i < len(s):
        if s[i].isalpha():
            r[i] = r[i].swapcase()
            i += 1
        else:
            break
    i = len(s) - 1
    while i >= 0:
        if s[i].isalpha():
            r[i] = r[i].swapcase()
            i -= 1
        else:
            break
    i = 0
    while i < len(s):
        if r[i].isalpha():
            i += 1
        else:
            break
    if i < len(s):
        r = r[i:][::-1] + r[:i]
    return "".join(r)

