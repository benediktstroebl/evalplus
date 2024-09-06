
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
    if not s:
        return ""
    new_string = []
    for i in s:
        if i.isalpha():
            new_string.append(i.upper() if i.islower() else i.lower())
        else:
            new_string.append(i)
    return "".join(new_string)[::-1]

