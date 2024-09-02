
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
    reverse = ''
    for i in s:
        if ord('a') <= ord(i) <= ord('z'):
            reverse += chr(ord(i) ^ 32)
        elif ord('A') <= ord(i) <= ord('Z'):
            reverse += chr(ord(i) ^ 32)
        else:
            reverse += i
    return reverse if reverse else s[::-1]
