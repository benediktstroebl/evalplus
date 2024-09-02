
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
    def is_letter(char):
        return ord('a') <= ord(char) <= ord('z') or ord('A') <= ord(char) <= ord('Z')
    if not is_letter(s[0]):
        return s[::-1]
    i = 0
    res = ''
    while i < len(s):
        if is_letter(s[i]):
            if s[i].islower():
                res += s[i].upper()
            else:
                res += s[i].lower()
            i += 1
        else:
            res += s[i]
            i += 1
    return res

