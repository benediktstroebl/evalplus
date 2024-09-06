
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
        return "0"
    elif s[0] == "#":
        return "#" + solve(s[1:])
    elif len(s) == 1:
        return s[0]
    else:
        start = 0
        for i in range(1, len(s)):
            if s[i].isalpha():
                if s[i-1] == s[i]:
                    start += 1
            else:
                start = i+1
            if start == len(s):
                return s[start-1:]
            elif s[start] == s[i-1].upper():
                s = s[:start] + s[start+1:].upper() + s[start:]
            else:
                s = s[:start] + s[start+1:].lower() + s[start:]
        return s

result = solve("1234")
