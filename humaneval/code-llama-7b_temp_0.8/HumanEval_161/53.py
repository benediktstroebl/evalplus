
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
    new_s = ''
    for i in range(len(s)):
        if s[i].islower():
            new_s += s[i].upper()
        elif s[i].isupper():
            new_s += s[i].lower()
        else:
            new_s += s[i]
    return new_s if new_s else s[::-1]

    # if not s.isdigit():
    #     return s.swapcase()
    # return s[::-1]

    # if not s.isdigit():
    #     return s.swapcase()
    # return s[::-1]

