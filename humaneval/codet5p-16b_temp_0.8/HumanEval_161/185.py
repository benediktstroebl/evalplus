
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

    import string
    temp = []
    for i in range(len(s)):
        if s[i] not in string.ascii_letters:
            temp.append(s[i])
        else:
            if s[i].isupper():
                temp.append(s[i].lower())
            else:
                temp.append(s[i].upper())
    
    return ''.join(temp)
    
    
