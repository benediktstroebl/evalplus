
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
    #2nd method
    s = list(s)
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].islower():
                s[i] = s[i].upper()
            else:
                s[i] = s[i].lower()
    return "".join(s)
    
    # 1st method
    # if len(s) == 0:
    #     return s[::-1]
    # s = list(s)
    # s = [c.swapcase() if c.isalpha() else c for c in s]
    # return "".join(s)

