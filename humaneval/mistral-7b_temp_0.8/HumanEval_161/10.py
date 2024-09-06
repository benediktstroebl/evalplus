
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
    if s == '': return ''
    elif s == ' ': return s
    elif s == ' ': return s
    else:
        l = []
        for x in s:
            if x.isalpha():
                if x.islower():
                    x = x.upper()
                else:
                    x = x.lower()
                l.append(x)
            else:
                l.append(x)
        return ''.join(l)


