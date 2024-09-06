
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
    print(s)
    s1 = ""
    for i in s:
        if ord('a') <= ord(i) <= ord('z'):
            s1 += i.swapcase()
        elif ord('A') <= ord(i) <= ord('Z'):
            s1 += i.lower()
        else:
            s1 += i
    print(s1)
    return s1
