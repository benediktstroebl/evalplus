
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
    s = list(s)
    for i, char in enumerate(s):
        if char.isalpha():
            if char.isupper():
                s[i] = char.lower()
            elif char.islower():
                s[i] = char.upper()
    s.reverse()
    return ''.join(s)
