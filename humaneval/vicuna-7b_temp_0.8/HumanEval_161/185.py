
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
    result = ""
    i = 0
    while i < len(s):
        if s[i] in string.ascii_lowercase:
            result = string.ascii_uppercase.maketrans(unicode(s[i], 'utf-8'), unicode(s[i], 'utf-8'))
            i += 1
        elif s[i] in string.ascii_uppercase:
            result = string.ascii_lowercase.maketrans(unicode(s[i], 'utf-8'), unicode(s[i], 'utf-8'))
            i += 1
        else:
            result += s[i]
            i += 1
    return result
