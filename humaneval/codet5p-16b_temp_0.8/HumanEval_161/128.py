
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

    import re
    if s == "":
        return s
    elif re.search("[a-zA-Z]",s):
        return "".join(i.swapcase() for i in s)
    else:
        return s[::-1]

