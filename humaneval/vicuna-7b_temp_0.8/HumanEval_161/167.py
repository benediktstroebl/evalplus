
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
    s_lower = s.lower()
    s_no_letters = ""
    s_result = ""
    i = 0
    while i < len(s_lower):
        c = s_lower[i]
        if c.isalpha():
            s_result += c.upper()
        elif c == " ":
            s_no_letters += s_no_letters
        elif s_no_letters:
            s_result += c
        i += 1
    return s_result
