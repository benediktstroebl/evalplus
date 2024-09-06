
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
    res=""
    for i in s:
        if i.isalpha():
            if i.islower():
                res+=i.upper()
            else:
                res+=i.lower()
        else:
            res+=i
    return res if res else s[::-1]

