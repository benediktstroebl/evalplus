
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
    new_s = ""
    for _ in s:
        if _.isalpha():
            if _.islower():
                new_s += _.upper()
            else:
                new_s += _.lower()
        else:
            new_s += _
    return new_s
