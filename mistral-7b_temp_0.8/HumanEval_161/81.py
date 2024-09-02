
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
    def is_lower(ch):
        if ch.isalpha():
            return ch.islower()
        return False
    def is_upper(ch):
        if ch.isalpha():
            return ch.isupper()
        return False
    def is_letter(ch):
        return ch.isalpha()
    res = ''
    for ch in s:
        if is_letter(ch):
            if is_lower(ch):
                res += ch.upper()
            else:
                res += ch.lower()
        else:
            res += ch
    return res
