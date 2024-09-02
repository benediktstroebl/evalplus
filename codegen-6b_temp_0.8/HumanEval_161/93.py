
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
    if not s:
        return ""
    result = list(reversed(s))
    for i in range(len(result)):
        if result[i].isalpha():
            if result[i].isupper():
                result[i] = result[i].lower()
            else:
                result[i] = result[i].upper()
        else:
            result[i] = result[i]
    return "".join(result)
    
