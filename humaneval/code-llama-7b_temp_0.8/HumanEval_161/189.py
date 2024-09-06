
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
    # a = "1234"
    # b = 'ab'
    # c = "#a@C"
    # d = "ab123"
    # e = "12ab34"
    # f = "12.34"
    # g = "12.34.5"
    # print(solve(a))
    # print(solve(b))
    # print(solve(c))
    # print(solve(d))
    # print(solve(e))
    # print(solve(f))
    # print(solve(g))


    if any(char.isalpha() for char in s):
        return "".join(char.upper() if char.islower() else char.lower() for char in s)
    else:
        return s[::-1]



