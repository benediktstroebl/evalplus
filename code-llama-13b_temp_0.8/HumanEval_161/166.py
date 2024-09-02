
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
    l = len(s)
    if l == 0:
        return s
    if s.find('a') == -1 or s.find('A') == -1:
        return s[::-1]
    
    new = ""
    for i in range(l):
        if s[i].isalpha():
            if s[i].isupper():
                new += s[i].lower()
            else:
                new += s[i].upper()
        else:
            new += s[i]
    return new

