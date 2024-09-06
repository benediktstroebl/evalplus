
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
    if not s:
        return "#" + s.upper()[::-1] + "#"
    else:
        for i in range(len(s)):
            if s[i].isalpha():
                if s[i].lower() != s[i]:
                    s = s.upper()[::-1] + s[i].lower() + s.upper()[i+1:]
                else:
                    s = s.upper()[::-1] + s[i].upper() + s.upper()[i+1:]
                break
        return s

s = input("Enter a string: ")
result = solve(s)
print(result)