
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
        return s
    result = []
    for i in range(len(s)):
        if s[i].lower() >='a' and s[i].lower() <= 'z':
            result.append(s[i].lower())
        elif s[i].upper() >='A' and s[i].upper() <= 'Z':
            result.append(s[i].upper())
        else:
            result.append(s[i])
    return "".join(result)
