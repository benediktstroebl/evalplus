
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
    n = len(s)
    if n == 0:
        return s[::-1]
    elif n == 1:
        return s.lower()
    elif s[0].isalpha():
        return s[0].swapcase() + solve(s[1:n])
    elif s[-1].isalpha():
        return solve(s[0:n-1]) + s[-1].swapcase()
    else:
        return solve(s[0:n-1]) + s[n-1]
