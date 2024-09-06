
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
    is_lower = False
    out = []
    for i in s:
        if i.isalpha():
            if is_lower:
                out.append(i.upper())
                is_lower = False
            else:
                out.append(i.lower())
                is_lower = True
        else:
            out.append(i)
    return "".join(out)

