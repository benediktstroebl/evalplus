
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
    string = ""
    i = 0
    while i < len(s):
        if s[i] in string.lowercase:
            string += s[i].upper()
        elif s[i] in string.uppercase:
            string += s[i].lower()
        else:
            string += s[i]
        i += 1
    return string

s = input("Enter string: ")
result = solve(s)
print(result)