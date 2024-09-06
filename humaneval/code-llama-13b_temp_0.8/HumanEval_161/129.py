
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
    if not "a" <= min(s) <= "z" and not "A" <= min(s) <= "Z":
        return s[::-1]
    return s.swapcase()
    # return s.swapcase() if "a" <= min(s) <= "z" or "A" <= min(s) <= "Z" else s[::-1]

