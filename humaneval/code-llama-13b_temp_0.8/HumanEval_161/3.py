
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
    return_str = ''
    has_letter = False
    for i in range(len(s)):
        if not s[i].isalpha():
            return_str += s[i]
        else:
            has_letter = True
            if s[i].islower():
                return_str += s[i].upper()
            else:
                return_str += s[i].lower()
    return s[::-1] if not has_letter else return_str

