
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
    n = len(s)
    def is_letter(i):
        return ord(s[i]) >= ord('a') and ord(s[i]) <= ord('z') or ord(s[i]) >= ord('A') and ord(s[i]) <= ord('Z')

    result = ""
    for i in range(n):
        if is_letter(i):
            result += s[i].upper() if s[i].isupper() else s[i].lower()
        else:
            result += s[i]
    return result

