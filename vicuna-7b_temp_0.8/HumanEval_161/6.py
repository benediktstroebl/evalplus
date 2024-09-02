
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
    s = s.upper()
    s = s.replace(" ", "")
    result = ""
    i = 0
    while i < len(s):
        c = s[i]
        if c.isalpha():
            result = chr(ord(c) ^ ord('a') - 1) if c.islower() else chr(ord(c) ^ ord('A') - 1)
        else:
            result += c
        i += 1
    return result