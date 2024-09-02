
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
    #solution
    # if s == "": return s
    # alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # for i in range(len(s)):
    #     if s[i] in alphabet:
    #         s[i] = alphabet[alphabet.index(s[i].lower())].upper()
    #     else:
    #         s[i] = s[i]
    # return s
    s = list(s)
    for i in range(len(s)):
        if s[i].isalpha():
            s[i] = s[i].lower() if s[i].islower() else s[i].upper()
        else:
            s[i] = s[i]
    return ''.join(s)
