
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
    # for i in range(len(s)):
    #     if s[i].isalpha():
    #         s[i] = s[i].swapcase()
    #     else:
    #         continue
    # if s.isalpha():
    #     s.reverse()
    # return s
    for i, c in enumerate(s):
        if c.isalpha():
            s = s[:i] + s[i:].swapcase()
            break
    if s.isalpha():
        return s[::-1]
    return s
