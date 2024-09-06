
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
    s = s.lower()
    # add space to the string
    s += " "
    reversed_chars = ""
    for char in s:
        if char.isalpha():
            if char.lower() == char:
                reversed_chars += chr(ord(char) - 1) + chr(ord(char) + 1)
            else:
                reversed_chars += chr(ord(char) + 1)
        else:
            reversed_chars += char
    return reversed_chars.strip()
