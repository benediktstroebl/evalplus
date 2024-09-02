
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
    s = list(s)
    letter = 0
    for i in range(len(s)):
        if s[i].isalpha():
            letter += 1

    if letter == 0:
        s = s[::-1]
    else:
        for i in range(len(s)):
            if s[i].isalpha():
                s[i] = s[i].swapcase()

    return "".join(s)
