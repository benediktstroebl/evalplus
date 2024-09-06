
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

    lst = list(s)
    new_lst = []
    for c in lst:
        if c.isalpha():
            if c.isupper():
                c = c.lower()
            else:
                c = c.upper()
        new_lst.append(c)
    return "".join(new_lst)

