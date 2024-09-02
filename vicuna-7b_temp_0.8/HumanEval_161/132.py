
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
    reversed_s = ""
    current_letter = ""
    for char in s:
        if char.isalpha():
            if current_letter.islower():
                reversed_s += current_letter.upper()
                current_letter = char.upper()
            else:
                current_letter += char
        else:
            reversed_s += char
        if current_letter.isalpha():
            reversed_s += current_letter.lower()
            current_letter = ""
    reversed_s += current_letter
    return reversed_s