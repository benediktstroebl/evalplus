
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
    s1 = ''.join([char.lower() if char.isupper() else char.upper() if char.islower() else char for char in s])
    if s1.isalpha():
        return s1[::-1]
    return s1
