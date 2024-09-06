
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
    result = ''
    letters = False
    for i in range(len(s)):
        if s[i].isalpha():
            letters = True
        if s[i].isalpha() and letters == True:
            if s[i].isupper():
                result += s[i].lower()
            else:
                result += s[i].upper()
        else:
            result += s[i]
    if letters == False:
        return result[::-1]
    return result

