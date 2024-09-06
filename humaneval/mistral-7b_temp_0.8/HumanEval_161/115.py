
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

    def _solve(s, result):
        if s:
            if s[0].isalpha():
                _solve(s[1:], result + s[0].swapcase())
            else:
                _solve(s[1:], result + s[0])
        else:
            return result[::-1]

    return _solve(s, "")
