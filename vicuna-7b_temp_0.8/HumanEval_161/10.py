
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
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].lower() == s[i].upper():
                result.append(s[i])
            else:
                result.append(s[i].title())
        else:
            result.append(s[i])
    return "".join(reversed(result))

s = input()
