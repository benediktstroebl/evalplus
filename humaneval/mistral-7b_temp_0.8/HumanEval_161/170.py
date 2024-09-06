
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
    letters = [i for i in s if i.isalpha()]
    numbers = [i for i in s if not i.isalpha()]
    output = []
    for letter in letters:
        if letter.isupper():
            output.append(letter.lower())
        else:
            output.append(letter.upper())
    output.extend(numbers)
    return "".join(output)
