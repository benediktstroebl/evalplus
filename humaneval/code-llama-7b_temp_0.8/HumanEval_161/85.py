
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

    for i in range(len(s)):
        if ord(s[i]) >= 65 and ord(s[i]) <= 90:
            result += s[i].lower()
        elif ord(s[i]) >= 97 and ord(s[i]) <= 122:
            result += s[i].upper()
        else:
            result += s[i]

    if len(result) == 0:
        return s
    else:
        return result[::-1]
