
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
    letters = list(s)
    for i in range(len(letters)):
        if letters[i].isalpha():
            if letters[i].islower():
                letters[i] = letters[i].upper()
            else:
                letters[i] = letters[i].lower()
    return ''.join(letters)
    
    
