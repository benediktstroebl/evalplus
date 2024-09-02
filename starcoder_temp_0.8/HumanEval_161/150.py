
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
    s1 = list(s)
    for i in range(len(s1)):
        if s1[i].isalpha():
            if s1[i].isupper():
                s1[i] = s1[i].lower()
            else:
                s1[i] = s1[i].upper()
    return "".join(s1)
