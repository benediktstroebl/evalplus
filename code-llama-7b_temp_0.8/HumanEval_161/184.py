
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

    def reverse(s):
        return s[::-1]

    def reverse_if_letter(c):
        if c.isalpha():
            return c.swapcase()
        return c

    return "".join(map(reverse_if_letter, s))
