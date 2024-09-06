
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
    return "".join([
        (c if c.isdigit() else c.swapcase())
        for c in s
    ])

    # a = ""
    # for c in s:
    #     if c.isalpha():
    #         a += c.swapcase()
    #     else:
    #         a += c
    # return a
    
    # s = s.swapcase()
    # return s if len(s.strip(s.lower())) == 0 else s.swapcase()

    # s = "".join(c.swapcase() if c.isalpha() else c for c in s)
    # return s if len(s.strip(s.lower())) == 0 else s.swapcase()

    # return s if len(s.strip(s.lower())) != 0 else s.swapcase()

    # if len(s.strip(s.lower())) == 0:
    #     return s.swapcase()

    # s = "".join(c.swapcase() if c.isalpha() else c for c in s)
    # return s.swapcase() if len(s.strip(s.lower())) == 0 else s

    # if len(s.strip(s.lower())) == 0:
    #     return s.swapcase()
    # return s.swapcase() if len(s.strip(s.lower())) == 0 else s

    # a = ""
    # for c in s:
    #     if c.isalpha():
    #         a += c.swapcase()
    #     else:
    #         a += c
    # return a if len(a.strip(a.lower())) == 0 else a.swapcase()

    # a = ""
    # for c in s:
    #     if c.isalpha():
    #         a += c.swapcase()
    #     else:
    #         a += c
    # return a if len(a.strip(a.lower())) == 0 else a.swapcase()

    # a = ""
    # for c in s:
    #     if c.isalpha():
    
