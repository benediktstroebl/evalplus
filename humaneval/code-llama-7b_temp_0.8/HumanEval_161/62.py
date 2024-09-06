
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
    result = []
    for letter in s:
        if letter.isalpha():
            if letter.isupper():
                result.append(letter.lower())
            else:
                result.append(letter.upper())
        else:
            result.append(letter)

    result = "".join(result)
    if len(result) == 0:
        return s[::-1]
    return result

