
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
    s = s.lower() # converting to lower case
    if not s.strip(): # removing leading and trailing spaces
        s = s[1:].lower() # taking the lowercase string
    else:
        s = s[:-1].lower() # taking the lowercase string except last

    result = ""
    for i in range(len(s)):
        if s[i].isalpha():
            result += s[i].upper()
        else:
            result += s[i]

    return result.lower()

s = "SaTaNdRa"
