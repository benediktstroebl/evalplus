
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
    # return s[::-1]
    
    l = list(s)
    for i in range(len(l)):
        if l[i].isalpha():
            l[i] = l[i].swapcase()
        else:
            pass
    if not l[-1].isalpha():
        l = l[::-1]
        return ''.join(l)
    else:
        return ''.join(l)
    # return l

