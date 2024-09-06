
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
    # check if string contains any letters
    letters = False
    for i in s:
        if i.isalpha():
            letters = True
            break
    if letters == True:
        # loop through string
        # if letter, change case
        # if not, keep the same
        out = ""
        for i in s:
            if i.isalpha():
                out += i.swapcase()
            else:
                out += i
    else:
        # reverse string
        out = s[::-1]
    return out

