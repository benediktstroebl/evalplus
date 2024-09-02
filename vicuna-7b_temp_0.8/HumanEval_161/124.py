
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
    s = s.upper()
    i = 0
    while i < len(s) and s[i] in string.ascii_uppercase or s[i] in string.ascii_lowercase:
        if s[i] in string.ascii_uppercase:
            s = s.replace(s[i], chr(ord(s[i])-32))
        elif s[i] in string.ascii_lowercase:
            s = s.replace(s[i], chr(ord(s[i])+32))
        i += 1
    return s

s = input("Enter a string: ")
result = solve(s)
