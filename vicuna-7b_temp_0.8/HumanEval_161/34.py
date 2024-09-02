
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
    def reverse_case(s):
        new_s = ""
        for char in s:
            if char.isalpha():
                new_s += char.upper()
            else:
                new_s += char
        return new_s

    if len(s) == 0:
        return s.upper()

    for i in range(len(s)):
        if s[i].isalpha():
            s = s.replace(s[i], s[i].upper(), 1)
        else:
            s = s.replace(s[i], '', 1)

    return reverse_case(s)
