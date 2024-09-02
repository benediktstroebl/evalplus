
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
    no_letters = True
    for char in s:
        if char.isalpha():
            no_letters = False
            break
    if no_letters:
        return s[::-1]
    else:
        result = ""
        for char in s:
            if char.isupper():
                result += char.lower()
            elif char.islower():
                result += char.upper()
            else:
                result += char
        return result

