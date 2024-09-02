
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
    # a = list(s)
    # i = 0
    # while i < len(a):
    #     if a[i].isalpha():
    #         if a[i].islower():
    #             a[i] = a[i].upper()
    #         else:
    #             a[i] = a[i].lower()
    #     i += 1
    # return "".join(a)
    return s.swapcase() if s.isalpha() else s[::-1]
