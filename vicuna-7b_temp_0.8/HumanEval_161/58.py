
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
    s = s.lower()
    i = 0
    result = ""
    while i < len(s):
        if s[i].isalpha():
            result = chr(ord(s[i]) - ord('a') + 26) + result
        elif s[i] == "#":
            result = "#" + result
        i += 1
    return result
