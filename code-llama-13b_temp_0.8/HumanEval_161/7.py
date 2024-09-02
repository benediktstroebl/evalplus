
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
    new_s = ""
    counter = 0
    # if s == "":
    #     return ""
    for i in range(len(s)-1, -1, -1):
        if not s[i].isalpha():
            new_s += s[i]
            counter = 0
        else:
            if s[i].islower():
                new_s += s[i].upper()
            else:
                new_s += s[i].lower()
            counter += 1
    if counter == 0:
        return new_s[::-1]
    else:
        return new_s

