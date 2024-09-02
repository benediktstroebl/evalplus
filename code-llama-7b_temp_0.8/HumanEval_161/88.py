
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
    flag = 0
    if len(s) == 0:
        return s
    for i in range(len(s)):
        if ord(s[i]) >= 97 and ord(s[i]) <= 122:
            result += s[i].upper()
            flag = 1
        elif ord(s[i]) >= 65 and ord(s[i]) <= 90:
            result += s[i].lower()
            flag = 1
        else:
            result += s[i]
    if flag == 0:
        return result[::-1]
    return result
