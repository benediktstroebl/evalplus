
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
    l = list(s)
    lower = [char for char in s if char.islower()]
    upper = [char for char in s if char.isupper()]
    reverse_lower = lower[::-1]
    reverse_upper = upper[::-1]
    l[0:len(lower)] = reverse_lower
    l[len(lower):] = reverse_upper
    return "".join(l)

