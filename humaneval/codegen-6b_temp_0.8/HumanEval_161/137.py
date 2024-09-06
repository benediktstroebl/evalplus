
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
    
    i = 0
    result = ""
    while i < len(s):
        if s[i] in string.ascii_letters:
            if s[i].isupper():
                result += s[i].lower()
            else:
                result += s[i].upper()
        else:
            result += s[i]
        i += 1
    return result
