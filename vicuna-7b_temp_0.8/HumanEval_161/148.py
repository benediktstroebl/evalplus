
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
    s = s.lower() # change to lowercase
    n = len(s)
    d = {}
    for i in range(n):
        c = s[i]
        if c.isalpha():
            if c.islower():
                d[i] = chr(ord(c) - ord('a') + 25)
            elif c.isupper():
                d[i] = chr(ord(c) - ord('A') + 25)
        else:
            d[i] = c
    result = ''
    for i in range(n):
        if i in d:
            result += d[i]
        else:
            result += s[i]
    return result
