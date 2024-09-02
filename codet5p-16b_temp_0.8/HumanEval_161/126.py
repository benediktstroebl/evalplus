
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

    i = 0
    j = len(s) - 1
    while i < j:
        if s[i].isalpha() and s[j].isalpha():
            if s[i].islower():
                s = s[:i] + s[i].upper() + s[i+1:j+1] + s[j].upper() + s[j+1:]
            else:
                s = s[:i] + s[i].lower() + s[i+1:j+1] + s[j].lower() + s[j+1:]
            i += 1
            j -= 1
        else:
            i += 1
            j -= 1
    return s
