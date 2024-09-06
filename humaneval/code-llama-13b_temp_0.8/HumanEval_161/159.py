
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

    letters = []
    for x in s:
        if x.isalpha():
            letters.append(x)

    new_string = ""
    if len(letters) == 0:
        new_string = s[::-1]
    else:
        for x in s:
            if x.isalpha():
                if x.isupper():
                    new_string += x.lower()
                elif x.islower():
                    new_string += x.upper()
                else:
                    new_string += x
            else:
                new_string += x

    return new_string
