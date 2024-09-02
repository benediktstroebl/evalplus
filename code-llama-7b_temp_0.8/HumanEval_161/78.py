
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
    new_str = ""
    for i in s:
        if i.isalpha():
            if i.islower():
                i = i.upper()
            else:
                i = i.lower()
        new_str += i
    if len(new_str) == 0:
        new_str = s[::-1]
    return new_str

