
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
    if len(s) == 0:
        return s
    else:
        i = 0
        while i < len(s) - 1:
            if s[i].isalpha():
                s[i:], s[i+1:] = s[i+1:], s[i:]
            elif s[i] == s[i+1]:
                i += 1
            else:
                s[i], s[i+1] = s[i+1], s[i]
        return s

s = input().lower()
result = solve(s)
