
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
    string = s
    lower_string = ""
    upper_string = ""
    for char in string:
        if char.isalpha():
            if char.islower():
                upper_string += char.upper()
            else:
                lower_string += char.lower()
        else:
            lower_string += char
    return "".join(upper_string.split(lower_string))
