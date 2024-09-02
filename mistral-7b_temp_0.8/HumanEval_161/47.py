
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
    ans = ""
    for c in s:
        if c.isalpha():
            ans += chr(ord(c) - ord('a' + ord('A'))) if c.isupper() else chr(ord(c) + ord('a' - 'A'))
        else:
            ans += c
    return ans
