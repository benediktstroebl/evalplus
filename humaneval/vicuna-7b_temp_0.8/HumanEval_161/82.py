
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
    if "letter" in s:
        s = s.replace("lower", "").replace("upper", "")
        s = s.replace("case", "")
        l = s.split("")
        for i in range(len(l)):
            if l[i] == " ":
                l[i] = chr(ord("a") + i)
        s = "".join(l)
    elif s:
        s = s.lower()
    return s
