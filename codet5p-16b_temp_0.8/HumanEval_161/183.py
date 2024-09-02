
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

    new_str = ""
    for i in s:
        if i.islower():
            new_str += i.upper()
        elif i.isupper():
            new_str += i.lower()
        else:
            new_str += i
    return new_str if new_str!= "" else s[::-1]

