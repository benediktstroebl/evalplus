
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
    s = s.lower() # convert to lowercase
    i = 0
    reversed_string = ""
    while i < len(s):
        if s[i].isalpha(): # check if the character is a letter
            if s[i].islower(): # check if the letter is in lowercase
                reversed_string += s[i].upper()
            else:
                reversed_string += s[i].lower()
        else:
            reversed_string += s[i]
        i += 1
    return reversed_string
