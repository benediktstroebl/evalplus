
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
    print("solve", s)
    if not s: return s
    new_string = s[0]
    for i in s[1:]:
        if i.isalpha():
            new_string = new_string + i.swapcase()
        else:
            new_string += i
    return new_string



