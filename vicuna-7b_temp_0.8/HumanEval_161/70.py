
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
    s = s.lower() # All lowercase
    result = ""
    last_c = ""
    for c in s:
        if c.isalpha():
            if c.isupper():
                result += c.upper()
                last_c = c.upper()
            elif c.islower():
                result += c.lower()
                last_c = c.lower()
            else:
                result += c
                last_c = c
        else:
            result += c
    return result + last_c * (len(s) % 2 == 0)
