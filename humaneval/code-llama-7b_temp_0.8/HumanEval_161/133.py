
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
    #sp = []
    #for char in s:
    #    if char.isalpha():
    #        sp.append(char.upper() if char.islower() else char.lower())
    #    else:
    #        sp.append(char)
    #return ''.join(sp[::-1])
    return ''.join(list(map(lambda x: x.upper() if x.islower() else x.lower(), s[::-1])))
