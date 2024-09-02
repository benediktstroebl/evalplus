
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
    def _solve(s):
        if not s:
            return s
        new_s = ""
        for i, c in enumerate(s):
            if c.isalpha():
                new_s += chr(ord(c) - 32)
            else:
                new_s += c
        return new_s
    return _solve(s)
