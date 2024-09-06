
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

    # # version 1
    # def solve(s):
    #     ret = ""
    #     for c in s:
    #         if c.isalpha():
    #             ret += c.swapcase()
    #         else:
    #             ret += c
    #     return ret

    # # version 2
    # def solve(s):
    #     return "".join(map(lambda c: c.swapcase() if c.isalpha() else c, s))

    # version 3
    return "".join(map(lambda c: c.swapcase() if c.isalpha() else c, s))

