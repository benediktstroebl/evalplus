
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

    
    return "".join(str.swapcase(s[i]) if not s[i].isalpha() else str.lower(s[i]) if s[i].isupper() else str.upper(s[i]) for i in range(len(s)))

    
