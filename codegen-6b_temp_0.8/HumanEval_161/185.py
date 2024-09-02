
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
    char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    f = len(s)
    l = []
    for e in range(f):
        try:
            if s[e] in char:
                if s[e].isupper():
                    l.append(s[e].lower())
                else:
                    l.append(s[e].upper())
            elif s[e] == ' ':
                l.append(' ')
            else:
                l.append(s[e])
        except IndexError:
            l.append(s[e])
    return ''.join(l)
