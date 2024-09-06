
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
    letters = []
    for i in range(len(s)):
        if s[i].isalpha() == True:
            letters.append(s[i])
    if len(letters) == 0:
        return s[::-1]
    else:
        for i in range(len(s)):
            if s[i].isalpha() == True:
                if s[i].isupper():
                    s = s[:i] + s[i].lower() + s[i+1:]
                elif s[i].islower():
                    s = s[:i] + s[i].upper() + s[i+1:]
    return s
    
