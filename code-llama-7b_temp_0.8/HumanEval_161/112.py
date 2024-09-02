
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
    # check if string has any letter in it
    if any(x.isalpha() for x in s):
        # use map with lambda to check if letter or not and if yes, reverse it
        return "".join(map(lambda x: x.swapcase() if x.isalpha() else x, s))
    else:
        # if string has no letter, then reverse the string
        return s[::-1]
