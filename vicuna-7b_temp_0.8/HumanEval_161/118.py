
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
    string = s.lower()
    if string:
        result = ""
        for char in string:
            if char.isalpha():
                result += char.upper()
            else:
                result += char
        return result
    else:
        result = s
        return result

string = input("Enter a string: ")
