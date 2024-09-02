
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
    result = ""
    for i in s:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            result += i.swapcase()
        elif ord(i) >= ord('A') and ord(i) <= ord('Z'):
            result += i
        else:
            result += i
    return result

assert solve("1234") == "4321"
assert solve("ab") == "AB"
assert solve("#a@C") == "#A@c"
assert solve("") == ""
assert solve(None) == ""