
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
    if s.isalpha():
        return s.swapcase()
    if s.isnumeric():
        return s[::-1]
    return s[::-1]

    # simpler version
    # if s.isalpha():
    #     return s.swapcase()
    # return s[::-1]

    # simpler version 2
    # if s.isalpha():
    #     return s.swapcase()
    # return s[::-1]

    # One more solution
    # return ''.join(x.upper() if x.islower() else x.lower() for x in s)

