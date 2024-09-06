
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

    s_list = list(s)
    res = []
    for ch in s_list:
        if ch.isalpha():
            if ch.isupper():
                res.append(ch.lower())
            else:
                res.append(ch.upper())
        else:
            res.append(ch)
    res = "".join(res)
    return res


