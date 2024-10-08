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
    for char in s:
        if char.isalpha():
            if char.islower():
                new_s += char.upper()
            elif char.isupper():
                new_s += char.lower()
        else:
            new_s += char
    if new_s.isalpha():
        return new_s
    else:
        return new_s[::-1]
