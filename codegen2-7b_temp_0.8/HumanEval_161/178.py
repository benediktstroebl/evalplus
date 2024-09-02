
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
    result = ""
    for s_i in s:
        if s_i.isalpha():
            if s_i.islower():
                result += s_i.upper()
            else:
                result += s_i.lower()
        else:
            result += s_i
    return result
