
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
    # bool is_letters = False
    result = []
    for char in s:
        if char.isalpha():
            result.append(char.swapcase())
            # is_letters = True
        else:
            result.append(char)
    if not any(char.isalpha() for char in s):
        return ''.join(result)[::-1]
    return ''.join(result)

