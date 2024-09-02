
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
    
    s = s.lower()
    if not s:
        return s
    
    new_string = ""
    for i in range(len(s)):
        if ord(s[i]) >= ord('a') and ord(s[i]) <= ord('z'):
            new_string += chr(ord(s[i]) - 32)
        else:
            new_string += s[i]
    return new_string
