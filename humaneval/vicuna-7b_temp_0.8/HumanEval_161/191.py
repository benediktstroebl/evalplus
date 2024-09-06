
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
    count = 0
    result = ""
    i = 0
    while i < len(s):
        if s[i].isalpha():
            if s[i] >= 'a' and s[i] <= 'z':
                result += s[i].upper()
            else:
                result += s[i].lower()
        else:
            result += s[i]
        i += 1
        count += 1
    if count % 2 == 0:
        result = result[::-1]
    return result
