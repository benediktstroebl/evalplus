
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
    l = len(s)
    for i in xrange(1, l + 1):
        if is_letter(s[i - 1]):
            if s[i - 1].isupper():
                result += s[i - 1].lower()
            else:
                result += s[i - 1].upper()
        else:
            result += s[i - 1]
    return result

