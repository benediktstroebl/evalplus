
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
    if len(s) == 0:
        return s[::-1]
    else:
        for i in range(1, len(s)):
            if s[i] == " ":
                continue
            elif s[i-1] == s[i]:
                s = s[:i] + s[i-1].upper() + s[i:]
            else:
                s = s[:i] + s[i].lower() + s[i+1:]
        return s

s = input("Enter a string: ")
result = solve(s)
print(result)