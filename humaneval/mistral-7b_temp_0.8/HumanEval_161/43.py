
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
    lst = list(s)
    for i in range(len(s)):
        if s[i] not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            continue
        if s[i] == s[i].lower():
            lst[i] = s[i].upper()
        else:
            lst[i] = s[i].lower()
    return ''.join(lst)
