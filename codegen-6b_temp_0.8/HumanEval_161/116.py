
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
    small = True
    for letter in s:
        if letter.isalpha():
            small = False
    if small:
        return s[::-1]
    else:
        result = ""
        for letter in s:
            if letter.isalpha():
                if letter.isupper():
                    result += letter.lower()
                else:
                    result += letter.upper()
            else:
                result += letter
        return result

