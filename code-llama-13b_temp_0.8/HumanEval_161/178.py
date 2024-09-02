
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
    # your code goes here
    # if s.isalpha() == False:
    #     return s[::-1]
    # else:
    #     return s.swapcase()

    # Alternative
    import re
    s = re.split(r'(?=[A-Z])', s, maxsplit=1)
    return s[-1].swapcase() if s[0].isalpha() else s[1][::-1]

