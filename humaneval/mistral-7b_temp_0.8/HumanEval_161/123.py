
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
    lower_letter = 0
    upper_letter = 0
    for letter in s:
        if letter.islower():
            s = s[:lower_letter] + letter.upper() + s[lower_letter + 1:]
            lower_letter += 1
        elif letter.isupper():
            s = s[:upper_letter] + letter.lower() + s[upper_letter + 1:]
            upper_letter += 1
        else:
            continue
    return s

