
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
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    upper_alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    #1234
    if s.isalpha() == False:
        return s[::-1]
    elif s.isalpha() == True:
        return ''.join(x if x.islower() else x.isupper() for x in s)
