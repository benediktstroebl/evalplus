
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
    s = s.lower() # make lowercase
    d = {}
    for c in s:
        if c.isalpha(): # check if the character is a letter
            d[c.lower()] = c.upper() # add the lowercase letter to the dictionary, with its uppercase equivalent
        else:
            d[c] = c # add the character to the dictionary, with itself
    r = ""
    for k, v in d.items():
        r += k # append the key to the result
        r += v # append the value to the result
    return r
