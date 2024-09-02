
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
    if not s:
        return "".join([chr(ord("A") - 1) for c in s])
    else:
        lower = True
        upper = True
        for i, c in enumerate(s):
            if c.isalpha():
                if upper and c.isupper():
                    upper = False
                    c = chr(ord(c) - 2)
                elif lower and c.islower():
                    lower = False
                    c = chr(ord(c) + 2)
            elif not c.isalpha():
                if lower:
                    lower = False
                elif upper:
                    upper = False
                c = chr(ord(c))
        return "".join([c for c in s if c.isalpha()])

s = input()
result = solve(s)
