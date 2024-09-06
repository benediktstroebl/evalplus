
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
    upper = [char.isupper() for char in s]
    if sum(upper) == 0:
        return s[::-1]
    res = []
    for i, upper in enumerate(s):
        if upper.isalpha():
            res.append(upper.upper() if upper.islower() else upper.lower())
        else:
            res.append(upper)
    return ''.join(res)

