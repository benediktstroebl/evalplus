
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
    #1.
    return s[::-1] if not s.isalnum() else s.swapcase()
    #2.
    # if s.isalnum():
    #     return s.swapcase()
    # else:
    #     return s[::-1]

    #3.
    # if not s.isalnum():
    #     return s[::-1]
    # else:
    #     return s.swapcase()
    #4.
    # if not s.isalnum():
    #     return s[::-1]
    # else:
    #     return s.swapcase()
