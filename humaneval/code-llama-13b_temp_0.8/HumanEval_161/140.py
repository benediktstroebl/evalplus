
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
    no_letters = True
    for c in s:
        if c.isalpha():
            no_letters = False
            break
    if no_letters:
        s = s[::-1]
    else:
        new_s = ""
        for c in s:
            if c.isalpha():
                if c.isupper():
                    new_s += c.lower()
                else:
                    new_s += c.upper()
            else:
                new_s += c
        s = new_s
    return s
