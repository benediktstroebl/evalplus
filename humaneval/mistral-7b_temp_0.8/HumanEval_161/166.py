
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

    # Write your code here
    l = []
    for i in s:
        if i.isalpha():
            l.append(i.upper() if i.isupper() else i.lower())
        else:
            l.append(i)
    return ''.join(l)

